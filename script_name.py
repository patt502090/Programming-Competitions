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
    for i, entry in enumerate(entries):
        full_path = os.path.join(dir_path, entry)
        safe_entry = entry.replace(" ", "%20")
        if os.path.isdir(full_path):
            lines.append(f"{prefix}├── **{entry}/**")
            lines.extend(md_list(full_path, prefix + "│   "))
            # เพิ่มบรรทัดว่างหลัง folder หลัก
            lines.append("")
        else:
            rel_path = os.path.relpath(full_path, start=".").replace("\\", "/")
            rel_path = rel_path.replace(" ", "%20")
            lines.append(f'{prefix}├── [{entry}]({rel_path})')
    # ลบบรรทัดว่างสุดท้ายถ้ามี
    if lines and lines[-1] == "":
        lines.pop()
    return lines

if __name__ == "__main__":
    lines = md_list(".")
    print("\n".join(lines))
