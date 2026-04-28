from pathlib import Path


REQUIRED_COLUMNS = {
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
}


def split_markdown_row(line: str) -> list[str]:
    """
    Split a simple markdown table row into cells.
    """
    line = line.strip()

    if not line.startswith("|") or not line.endswith("|"):
        return []

    return [cell.strip() for cell in line.strip("|").split("|")]


def is_separator_row(cells: list[str]) -> bool:
    """
    Check whether a markdown table row is a separator row.
    """
    if not cells:
        return False

    return all(set(cell.replace(":", "").replace("-", "")) == set() for cell in cells)


def extract_index_table_lines(lines: list[str]) -> list[str]:
    """
    Extract the markdown table immediately below the "## Index" heading.
    """
    in_index_section = False
    table_lines: list[str] = []

    for line in lines:
        stripped = line.strip()

        if stripped == "## Index":
            in_index_section = True
            continue

        if in_index_section and stripped.startswith("## "):
            break

        if not in_index_section:
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            table_lines.append(line)
        elif table_lines:
            break

    return table_lines


def parse_index(index_path: Path) -> list[dict[str, str]]:
    """
    Parse index.md and return paper rows as dictionaries.
    """
    if not index_path.exists():
        raise FileNotFoundError(f"index.md not found: {index_path}")

    lines = index_path.read_text(encoding="utf-8").splitlines()
    table_lines = extract_index_table_lines(lines)

    if len(table_lines) < 2:
        raise ValueError('No markdown table found under "## Index" in index.md')

    header = split_markdown_row(table_lines[0])
    separator = split_markdown_row(table_lines[1])

    if not header or not is_separator_row(separator):
        raise ValueError("Invalid markdown table format in index.md")

    missing_columns = REQUIRED_COLUMNS - set(header)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Missing required columns in index.md: {missing}")

    rows: list[dict[str, str]] = []

    for line in table_lines[2:]:
        cells = split_markdown_row(line)

        if len(cells) != len(header):
            print(f"[skip] malformed row: {line}")
            continue

        row = dict(zip(header, cells))

        if not row.get("ID") or not row.get("File Name") or not row.get("Folder"):
            print(f"[skip] missing required field: {line}")
            continue

        rows.append(row)

    return rows
