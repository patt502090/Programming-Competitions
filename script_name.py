import os

IGNORE_DIRS = {'.git', '.cph'}

def list_dir_tree(root_dir):
    tree_lines = []

    def walk(dir_path, prefix=""):
        # เอา dir ที่จะข้ามออก
        try:
            entries = sorted(os.listdir(dir_path))
        except PermissionError:
            return

        # แยกโฟลเดอร์กับไฟล์
        dirs = [e for e in entries if os.path.isdir(os.path.join(dir_path, e)) and e not in IGNORE_DIRS]
        files = [e for e in entries if os.path.isfile(os.path.join(dir_path, e))]

        # แสดงโฟลเดอร์
        for i, d in enumerate(dirs):
            connector = "├── "
            if i == len(dirs) - 1 and not files:
                connector = "└── "
            rel_path = os.path.relpath(os.path.join(dir_path, d), root_dir).replace("\\", "/")
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

def generate_summary(root_dir):
    header = "# Project Structure\n\n"
    tree = list_dir_tree(root_dir)
    return header + tree + "\n"

def update_readme(readme_path, summary):
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = ["# Project\n\n"]

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
        f.write("\n\n")
        f.write(summary)

if __name__ == "__main__":
    root = "."
    readme = "README.md"
    summary_text = generate_summary(root)
    update_readme(readme, summary_text)
    print("README.md updated successfully!")
