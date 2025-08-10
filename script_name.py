import os

IGNORE_DIRS = {'.git', '.cph'}

def should_ignore(name):
    # ละเว้น folder/file ที่ชื่อเป็น .git, .cph หรือ เริ่มต้นด้วย '.' (hidden)
    return name in IGNORE_DIRS or name.startswith('.')

def list_dir_tree(root_dir):
    tree_lines = []

    def walk(dir_path, prefix=""):
        try:
            entries = sorted(os.listdir(dir_path))
        except PermissionError:
            return

        # กรองชื่อที่ไม่ต้องการ
        entries = [e for e in entries if not should_ignore(e)]

        dirs = [e for e in entries if os.path.isdir(os.path.join(dir_path, e))]
        files = [e for e in entries if os.path.isfile(os.path.join(dir_path, e))]

        # แสดงโฟลเดอร์
        for i, d in enumerate(dirs):
            connector = "├── "
            if i == len(dirs) - 1 and not files:
                connector = "└── "
            tree_lines.append(f"{prefix}{connector}**{d}/**")
            new_prefix = prefix + ("│   " if connector == "├── " else "    ")
            walk(os.path.join(dir_path, d), new_prefix)

        # แสดงไฟล์
        for i, f in enumerate(files):
            connector = "├── "
            if i == len(files) - 1:
                connector = "└── "
            rel_path = os.path.relpath(os.path.join(dir_path, f), root_dir).replace("\\", "/")
            tree_lines.append(f"{prefix}{connector}[{f}]({rel_path})")

    walk(root_dir)
    return "\n".join(tree_lines)

if __name__ == "__main__":
    root = "."
    print(list_dir_tree(root))
