from __future__ import annotations

import re
from pathlib import Path

from src.config import INDEX_PATH, ROOT_DIR, TARGET_FOLDERS
from src.folder_manager import add_folder


INDEX_COLUMNS = [
    "ID",
    "File Name",
    "Full Title",
    "Year",
    "Folder",
    "Link",
    "Tags",
    "Priority",
    "Reading Note",
    "Note",
]

PLACEHOLDER_LINKS = {"", "-", "to add", "tbd", "none", "링크_추가"}


def clean_cell(value: str) -> str:
    return value.strip().strip("`").strip()


def prompt_value(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{label}{suffix}: ").strip()
    return value or default


def prompt_choice(label: str, options: list[tuple[str, str]]) -> str:
    """
    Prompt a numbered choice.

    options: list of (value, display_label)
    """
    print(f"\n{label}")
    for idx, (_, display) in enumerate(options):
        print(f"[{idx}] {display}")

    while True:
        raw = input("Select number: ").strip()
        if raw.isdigit():
            selected = int(raw)
            if 0 <= selected < len(options):
                return options[selected][0]
        print("Invalid selection. Try again.")


def normalize_file_name(file_name: str) -> str:
    file_name = clean_cell(file_name)
    if not file_name.lower().endswith(".pdf"):
        file_name = f"{file_name}.pdf"
    return file_name


def short_name_from_file_name(file_name: str) -> str:
    file_name = clean_cell(file_name)
    if file_name.lower().endswith(".pdf"):
        return file_name[:-4]
    return file_name


def default_reading_note(paper_id: str, file_name: str) -> str:
    short_name = short_name_from_file_name(file_name)
    short_name = re.sub(r"^\d{4}_", "", short_name)
    short_name = re.sub(r"[^A-Za-z0-9_]+", "_", short_name).strip("_")
    return f"./99_Meta/reading_notes/{paper_id}_{short_name}.md"


def id_prefix(paper_id: str) -> str:
    match = re.match(r"([A-Za-z]+)(\d+)$", clean_cell(paper_id))
    return match.group(1) if match else clean_cell(paper_id)


def id_number(paper_id: str) -> int:
    match = re.match(r"([A-Za-z]+)(\d+)$", clean_cell(paper_id))
    return int(match.group(2)) if match else 0


def id_number_width(paper_id: str) -> int:
    match = re.match(r"([A-Za-z]+)(\d+)$", clean_cell(paper_id))
    return len(match.group(2)) if match else 0


def next_id_for_prefix(prefix: str, existing_ids: set[str]) -> str:
    numbers = [
        id_number(paper_id)
        for paper_id in existing_ids
        if id_prefix(paper_id) == prefix and id_number(paper_id) > 0
    ]
    next_number = max(numbers, default=0) + 1
    width = max(
        [id_number_width(paper_id) for paper_id in existing_ids if id_prefix(paper_id) == prefix]
        or [3]
    )
    return f"{prefix}{next_number:0{width}d}"


def folder_prefixes(existing_papers: list[dict[str, str]]) -> dict[str, str]:
    prefixes: dict[str, str] = {}

    for paper in existing_papers:
        folder = clean_cell(paper.get("Folder", ""))
        paper_id = clean_cell(paper.get("ID", ""))
        prefix = id_prefix(paper_id)

        if folder and prefix and prefix != paper_id:
            prefixes.setdefault(folder, prefix)

    return prefixes


def suggest_prefix_for_folder(folder: str) -> str:
    _, _, name = folder.partition("_")
    words = [word for word in name.split("_") if word]

    if not words:
        return folder.upper()

    if len(words) == 1:
        return words[0][:3].upper()

    return "".join(word[0].upper() for word in words)


def next_id_for_folder(folder: str, existing_papers: list[dict[str, str]]) -> tuple[str, bool]:
    existing_ids = {clean_cell(paper.get("ID", "")) for paper in existing_papers}
    known_prefixes = folder_prefixes(existing_papers)
    prefix = known_prefixes.get(folder)

    if prefix:
        return next_id_for_prefix(prefix, existing_ids), False

    prefix = suggest_prefix_for_folder(folder)
    return next_id_for_prefix(prefix, existing_ids), True


def prompt_paper_id(folder: str, existing_papers: list[dict[str, str]]) -> str:
    suggestion, is_new_prefix = next_id_for_folder(folder, existing_papers)

    if is_new_prefix:
        return prompt_value("ID", suggestion)

    print(f"\nID: {suggestion}")
    return suggestion


def prompt_folder(allow_new: bool = False) -> str:
    options = [(folder, folder) for folder in sorted(TARGET_FOLDERS)]

    print("\nSelect Folder")
    for idx, (_, display) in enumerate(options):
        print(f"[{idx}] {display}")
    if allow_new:
        print("[99] Add New Folder")

    while True:
        raw = input("Select number: ").strip()

        if allow_new and raw == "99":
            folder = prompt_value("New Folder")
            add_folder(folder)
            return folder

        if raw.isdigit():
            selected = int(raw)
            if 0 <= selected < len(options):
                return options[selected][0]

        print("Invalid selection. Try again.")


def prompt_priority() -> str:
    options = [("Low", "Low"), ("Medium", "Medium"), ("High", "High")]

    print("\nPriority")
    for idx, (_, display) in enumerate(options, start=1):
        print(f"[{idx}] {display}")

    while True:
        raw = input("Select number: ").strip()
        if raw.isdigit():
            selected = int(raw)
            if 1 <= selected <= len(options):
                return options[selected - 1][0]
        print("Invalid selection. Try again.")


def papers_in_folder(
    existing_papers: list[dict[str, str]],
    folder: str,
) -> list[dict[str, str]]:
    return [
        paper
        for paper in existing_papers
        if clean_cell(paper.get("Folder", "")) == folder
    ]


def prompt_existing_paper_id(existing_papers: list[dict[str, str]], folder: str) -> str:
    folder_papers = papers_in_folder(existing_papers, folder)

    if not folder_papers:
        raise ValueError(f"No papers found in folder: {folder}")

    options = [
        (
            clean_cell(paper.get("ID", "")),
            f"{clean_cell(paper.get('ID', ''))} - {paper.get('Full Title', '')}",
        )
        for paper in folder_papers
        if clean_cell(paper.get("ID", ""))
    ]

    print("\nSelect Paper to Delete")
    for idx, (_, display) in enumerate(options):
        print(f"[{idx}] {display}")

    while True:
        raw = input("Select number: ").strip()

        if raw.isdigit():
            selected = int(raw)
            if 0 <= selected < len(options):
                return options[selected][0]

        print("Invalid selection. Try again.")


def markdown_link(label: str, path: str) -> str:
    return f"[{label}]({path})"


def validate_markdown_cells(row: dict[str, str]) -> None:
    for key, value in row.items():
        if "|" in value:
            raise ValueError(f"Markdown table cell cannot contain '|': {key}")


def format_cell(column: str, value: str) -> str:
    value = value.strip()

    if column in {"File Name", "Folder"} and value:
        return f"`{clean_cell(value)}`"

    return value


def format_index_row(row: dict[str, str]) -> str:
    validate_markdown_cells(row)
    cells = [format_cell(column, row.get(column, "")) for column in INDEX_COLUMNS]
    return "| " + " | ".join(cells) + " |"


def find_index_table_end(lines: list[str]) -> int:
    in_index = False
    saw_table = False

    for idx, line in enumerate(lines):
        stripped = line.strip()

        if stripped == "## Index":
            in_index = True
            continue

        if in_index and stripped.startswith("## "):
            return idx

        if not in_index:
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            saw_table = True
            continue

        if saw_table:
            return idx

    return len(lines)


def create_reading_note_if_missing(reading_note: str, paper_id: str, title: str) -> None:
    if not reading_note.startswith("./"):
        return

    note_path = ROOT_DIR / reading_note[2:]

    if note_path.exists():
        return

    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(
        "\n".join(
            [
                f"# {paper_id} - {title}",
                "",
                "> Metadata: see `../../index.md`",
                "",
                "## Summary",
                "-",
                "",
                "## Key Idea",
                "-",
                "",
                "## Contribution",
                "-",
                "",
                "## Note",
                "-",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"[created] {note_path.relative_to(ROOT_DIR)}")


def build_paper_row(args, existing_papers: list[dict[str, str]]) -> dict[str, str]:
    existing_ids = {clean_cell(paper.get("ID", "")) for paper in existing_papers}

    folder = args.folder or prompt_folder(allow_new=True)
    folder = clean_cell(folder)
    if folder not in TARGET_FOLDERS:
        valid = ", ".join(sorted(TARGET_FOLDERS))
        raise ValueError(f"Unknown folder: {folder}. Valid folders: {valid}")

    paper_id = args.paper_id or prompt_paper_id(folder, existing_papers)
    paper_id = clean_cell(paper_id)
    if not paper_id:
        raise ValueError("ID is required.")
    if paper_id in existing_ids:
        raise ValueError(f"Duplicate paper ID: {paper_id}")

    file_name = args.file_name or prompt_value("File Name")
    file_name = normalize_file_name(file_name)

    title = args.title or prompt_value("Full Title")
    if not title:
        raise ValueError("Full Title is required.")

    year = args.year or prompt_value("Year")
    if not year:
        raise ValueError("Year is required.")

    link = args.link or prompt_value("Link", "-")
    tags = args.tags or prompt_value("Tags", "-")
    priority = args.priority or prompt_priority()
    note = args.note or prompt_value("Note", "")

    reading_note = args.reading_note
    if reading_note is None:
        default_note = default_reading_note(paper_id, file_name)
        reading_note = prompt_value("Reading Note", default_note)

    if clean_cell(reading_note):
        reading_note = markdown_link("note", reading_note)

    return {
        "ID": paper_id,
        "File Name": file_name,
        "Full Title": title,
        "Year": year,
        "Folder": folder,
        "Link": "" if link.lower() in PLACEHOLDER_LINKS else link,
        "Tags": tags,
        "Priority": priority,
        "Reading Note": reading_note,
        "Note": note,
    }


def append_paper_to_index(row: dict[str, str]) -> None:
    lines = INDEX_PATH.read_text(encoding="utf-8-sig").splitlines()
    insert_at = find_index_table_end(lines)

    lines.insert(insert_at, format_index_row(row))
    INDEX_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[updated] added {row['ID']} to index.md")


def remove_paper_from_index(paper_id: str) -> None:
    lines = INDEX_PATH.read_text(encoding="utf-8-sig").splitlines()
    target_prefix = f"| {paper_id} |"
    kept = [line for line in lines if not line.startswith(target_prefix)]

    if len(kept) == len(lines):
        raise ValueError(f"Paper ID not found in index.md: {paper_id}")

    INDEX_PATH.write_text("\n".join(kept) + "\n", encoding="utf-8")
    print(f"[updated] removed {paper_id} from index.md")


def add_paper(args, existing_papers: list[dict[str, str]]) -> None:
    row = build_paper_row(args, existing_papers)
    append_paper_to_index(row)

    reading_note = row.get("Reading Note", "")
    match = re.search(r"\]\(([^)]+)\)", reading_note)
    if match:
        create_reading_note_if_missing(match.group(1), row["ID"], row["Full Title"])


def delete_paper(args, existing_papers: list[dict[str, str]]) -> None:
    if args.del_paper_id:
        paper_id = args.del_paper_id
    else:
        folder = args.folder or prompt_folder()
        folder = clean_cell(folder)
        if folder not in TARGET_FOLDERS:
            valid = ", ".join(sorted(TARGET_FOLDERS))
            raise ValueError(f"Unknown folder: {folder}. Valid folders: {valid}")
        paper_id = prompt_existing_paper_id(existing_papers, folder)

    paper_id = clean_cell(paper_id)

    if not paper_id:
        raise ValueError("ID is required.")

    remove_paper_from_index(paper_id)
