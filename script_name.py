import os

IGNORE_DIRS = {'.git', '.cph'}

def should_ignore(name):
    return name in IGNORE_DIRS or name.startswith('.')

def md_list(dir_path, prefix=""):
    lines = []
    try:
        entries = sorted(os.listdir(dir_path))
    except Exception:
        return lines

    entries = [e for e in entries if not should_ignore(e)]
    for entry in entries:
        full_path = os.path.join(dir_path, entry)
        safe_name = entry.replace(" ", "%20")
        if os.path.isdir(full_path):
            lines.append(f"{prefix}- **{entry}/**")
            lines.extend(md_list(full_path, prefix + "  "))
        else:
            rel_path = os.path.relpath(full_path, start=".").replace("\\", "/")
            lines.append(f'{prefix}- [{entry}]({rel_path})')
    return lines

if __name__ == "__main__":
    lines = md_list(".")
    print("\n".join(lines))
