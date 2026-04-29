from __future__ import annotations

import argparse
from collections import defaultdict

from src.config import INDEX_PATH, ROOT_DIR, TARGET_FOLDERS, folder_meta_filename
from src.folder_manager import add_folder, remove_folder
from src.index_manager import add_paper, delete_paper
from src.index_parser import parse_index


def clean_cell(value: str) -> str:
    """
    Remove markdown code quotes and extra spaces.
    """
    return value.strip().strip("`").strip()


def make_markdown_link(short_name: str, url: str) -> str:
    """
    Make markdown link from short name and URL.

    If URL is empty or not ready, return plain short name.
    """
    short_name = clean_cell(short_name)
    url = url.strip()

    if not url or url.lower() in {"-", "to add", "tbd", "none", "링크_추가"}:
        return short_name

    return f"[{short_name}]({url})"


def make_short_name(paper: dict[str, str]) -> str:
    """
    Return Short Name when present, otherwise derive it from File Name.
    """
    short_name = clean_cell(paper.get("Short Name", ""))

    if short_name:
        return short_name

    file_name = clean_cell(paper.get("File Name", ""))

    if file_name.lower().endswith(".pdf"):
        return file_name[:-4]

    return file_name


def validate_folders(papers: list[dict[str, str]]) -> bool:
    """
    Validate folder names in index.md.

    Returns True if all folders are valid.
    """
    is_valid = True

    folders = {
        clean_cell(paper.get("Folder", ""))
        for paper in papers
        if paper.get("Folder")
    }

    unknown_folders = sorted(
        folder for folder in folders
        if folder and folder not in TARGET_FOLDERS
    )

    if unknown_folders:
        is_valid = False
        print("[warn] unknown folders found in index.md:")

        for folder in unknown_folders:
            print(f"  - {folder}")

    return is_valid


def group_papers_by_folder(
    papers: list[dict[str, str]],
) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)

    for paper in papers:
        folder = clean_cell(paper.get("Folder", ""))

        if not folder:
            continue

        grouped[folder].append(paper)

    return grouped


def generate_folder_meta_content(
    folder: str,
    papers: list[dict[str, str]],
) -> str:
    lines = [
        f"# {folder} Metadata",
        "",
        "자세한 메타데이터는 `../index.md`에서 관리한다.",
        "",
        "## Papers",
        "",
    ]

    if not papers:
        lines.append("-")
        lines.append("")
        return "\n".join(lines)

    for paper in papers:
        paper_id = clean_cell(paper.get("ID", ""))
        short_name = make_short_name(paper)
        link = paper.get("Link", "").strip()

        if not paper_id or not short_name:
            continue

        lines.append(f"- {paper_id}: {make_markdown_link(short_name, link)}")

    lines.append("")
    return "\n".join(lines)


def generate_folder_meta_files(papers: list[dict[str, str]]) -> None:
    grouped = group_papers_by_folder(papers)

    for folder in sorted(TARGET_FOLDERS):
        folder_path = ROOT_DIR / folder
        folder_path.mkdir(parents=True, exist_ok=True)

        output_path = folder_path / folder_meta_filename(folder)
        papers_in_folder = grouped.get(folder, [])

        content = generate_folder_meta_content(folder, papers_in_folder)
        output_path.write_text(content, encoding="utf-8")

        print(f"[generated] {output_path.relative_to(ROOT_DIR)}")


def run_check(papers: list[dict[str, str]]) -> None:
    validate_folders(papers)
    print(f"[info] loaded {len(papers)} papers from index.md")
    print("[info] check complete. No files generated.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate folder-level *_meta.md files from index.md."
    )

    parser.add_argument(
        "--check",
        action="store_true",
        help="Parse and validate index.md without generating folder metadata files.",
    )
    parser.add_argument(
        "--add-folder",
        metavar="FOLDER",
        help="Register a topic folder and create its folder metadata file.",
    )
    parser.add_argument(
        "--remove-folder",
        metavar="FOLDER",
        help="Unregister a topic folder and remove it if it is empty.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow unregistering a folder that is still referenced in index.md.",
    )
    parser.add_argument(
        "--add-paper",
        action="store_true",
        help="Interactively add a paper row to index.md and regenerate metadata files.",
    )
    parser.add_argument(
        "--del-paper",
        nargs="?",
        const="",
        dest="del_paper_id",
        metavar="ID",
        help="Delete a paper row from index.md by ID, or choose interactively.",
    )
    parser.add_argument("--id", dest="paper_id", help="Paper ID, for example TRN003.")
    parser.add_argument("--file-name", help="Local PDF file name.")
    parser.add_argument("--title", help="Full paper title.")
    parser.add_argument("--year", help="Publication or preprint year.")
    parser.add_argument("--folder", help="Target folder, for example 02_Training.")
    parser.add_argument("--link", help="Original online paper link.")
    parser.add_argument("--tags", help="Comma-separated tags.")
    parser.add_argument("--priority", help="Reading priority.")
    parser.add_argument("--reading-note", help="Reading note path.")
    parser.add_argument("--note", help="Free-form note.")

    args = parser.parse_args()

    papers = parse_index(INDEX_PATH)

    if args.add_folder and args.remove_folder:
        raise SystemExit("Use only one of --add-folder or --remove-folder.")

    if args.add_paper and args.del_paper_id is not None:
        raise SystemExit("Use only one of --add-paper or --del-paper.")

    if (args.add_paper or args.del_paper_id is not None) and (
        args.add_folder or args.remove_folder
    ):
        raise SystemExit("Use paper management separately from folder management commands.")

    if args.add_paper:
        add_paper(args, papers)
        papers = parse_index(INDEX_PATH)
        validate_folders(papers)
        generate_folder_meta_files(papers)
        return

    if args.del_paper_id is not None:
        delete_paper(args, papers)
        papers = parse_index(INDEX_PATH)
        validate_folders(papers)
        generate_folder_meta_files(papers)
        return

    if args.add_folder:
        add_folder(args.add_folder)
        papers = parse_index(INDEX_PATH)
        validate_folders(papers)
        generate_folder_meta_files(papers)
        return

    if args.remove_folder:
        remove_folder(args.remove_folder, papers, force=args.force)
        papers = parse_index(INDEX_PATH)
        validate_folders(papers)
        generate_folder_meta_files(papers)
        return

    if args.check:
        run_check(papers)
        return

    validate_folders(papers)
    print(f"[info] loaded {len(papers)} papers from index.md")

    generate_folder_meta_files(papers)


if __name__ == "__main__":
    main()
