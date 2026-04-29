from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

INDEX_PATH = ROOT_DIR / "index.md"

TARGET_FOLDERS = {
    "00_Inbox",
    "01_Survey",
    "02_Training",
    "03_Retrieval",
    "04_Evaluation",
    "05_Systems",
    "06_ML",
    "07_Agents",
    "08_Domain",
}


def folder_meta_filename(folder: str) -> str:
    """
    Return the generated metadata filename for a topic folder.

    Examples:
    - 00_Inbox -> Inbox_meta.md
    - 01_Survey -> Survey_meta.md
    - 05_Systems -> Systems_meta.md
    """
    _, _, name = folder.partition("_")
    base_name = name or folder
    return f"{base_name}_meta.md"
