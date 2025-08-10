import os
import urllib.parse

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
        if os.path.isdir(full_path):
            lines.append(f"{prefix}- **{entry}/**")
            lines.extend(md_list(full_path, prefix + "  "))
        else:
            rel_path = os.path.relpath(full_path, start=".").replace("\\", "/")
            rel_path = urllib.parse.quote(rel_path)
            lines.append(f'{prefix}- [{entry}]({rel_path})')
    return lines

if __name__ == "__main__":
    lines = md_list(".")
    output = "\n".join(lines) 

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(output + "\n")

