from __future__ import annotations

import re

from src.config import INDEX_PATH, ROOT_DIR, TARGET_FOLDERS, folder_meta_filename


CONFIG_PATH = ROOT_DIR / "src" / "config.py"
INDEX_FILE_NAME = INDEX_PATH.name
FOLDER_NAME_PATTERN = re.compile(r"^[0-9]{2}_[A-Za-z0-9_]+$")


def validate_folder_name(folder: str) -> None:
    """
    Validate managed topic folder names.
    """
    if not FOLDER_NAME_PATTERN.match(folder):
        raise ValueError(
            "Folder names must match NN_Name, for example 05_Models or 06_Agents."
        )


def write_target_folders(folders: set[str]) -> None:
    """
    Rewrite TARGET_FOLDERS in src/config.py.
    """
    folder_lines = "\n".join(f'    "{folder}",' for folder in sorted(folders))
    content = f'''from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

INDEX_PATH = ROOT_DIR / "index.md"

TARGET_FOLDERS = {{
{folder_lines}
}}


def folder_meta_filename(folder: str) -> str:
    """
    Return the generated metadata filename for a topic folder.

    Examples:
    - 00_Inbox -> Inbox_meta.md
    - 01_Fine_Tuning -> Fine_Tuning_meta.md
    - 02_RAG -> RAG_meta.md
    """
    _, _, name = folder.partition("_")
    base_name = name or folder
    return f"{{base_name}}_meta.md"
'''
    CONFIG_PATH.write_text(content, encoding="utf-8")


def add_folder(folder: str) -> None:
    """
    Add a managed topic folder and create its folder metadata file.
    """
    validate_folder_name(folder)

    if folder in TARGET_FOLDERS:
        print(f"[info] folder already registered: {folder}")
    else:
        TARGET_FOLDERS.add(folder)
        write_target_folders(TARGET_FOLDERS)
        print(f"[updated] registered folder in src/config.py: {folder}")

    folder_path = ROOT_DIR / folder
    folder_path.mkdir(parents=True, exist_ok=True)

    meta_path = folder_path / folder_meta_filename(folder)
    if not meta_path.exists():
        meta_path.write_text(make_empty_folder_meta_content(folder), encoding="utf-8")
        print(f"[created] {meta_path.relative_to(ROOT_DIR)}")
    else:
        print(f"[info] folder metadata already exists: {meta_path.relative_to(ROOT_DIR)}")


def remove_folder(
    folder: str,
    papers: list[dict[str, str]],
    force: bool = False,
) -> None:
    """
    Remove a managed topic folder from config and delete the directory only if safe.
    """
    validate_folder_name(folder)

    referenced_papers = [
        paper for paper in papers if paper.get("Folder", "").strip().strip("`") == folder
    ]

    if referenced_papers and not force:
        ids = ", ".join(paper.get("ID", "") for paper in referenced_papers)
        raise RuntimeError(
            f"Folder is still referenced in {INDEX_FILE_NAME}: {folder} ({ids}). "
            "Move those rows first, or rerun with --force to unregister only."
        )

    if folder in TARGET_FOLDERS:
        TARGET_FOLDERS.remove(folder)
        write_target_folders(TARGET_FOLDERS)
        print(f"[updated] unregistered folder in src/config.py: {folder}")
    else:
        print(f"[info] folder is not registered: {folder}")

    folder_path = ROOT_DIR / folder
    if not folder_path.exists():
        return

    contents = list(folder_path.iterdir())
    removable_contents = [
        item
        for item in contents
        if item.is_file() and item.name == folder_meta_filename(folder)
    ]

    if len(contents) == len(removable_contents):
        for item in removable_contents:
            item.unlink()
        folder_path.rmdir()
        print(f"[removed] {folder}")
    else:
        print(f"[kept] folder contains files; directory was not deleted: {folder}")


def make_empty_folder_meta_content(folder: str) -> str:
    return "\n".join(
        [
            f"# {folder} Metadata",
            "",
            "자세한 메타데이터는 `../index.md`에서 관리한다.",
            "",
            "## Papers",
            "",
            "-",
            "",
        ]
    )
