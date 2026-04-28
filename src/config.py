from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

INDEX_PATH = ROOT_DIR / "index.md"

TARGET_FOLDERS = {
    "00_Inbox",
    "01_Fine_Tuning",
    "02_RAG",
    "03_ML",
    "04_Application",
    "05_Models",
    "06_test",
}


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
    return f"{base_name}_meta.md"
