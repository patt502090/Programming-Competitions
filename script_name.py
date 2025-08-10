import os

def generate_summary(root_dir):
    summary = "## โฟลเดอร์และไฟล์ในโปรเจกต์\n\n"
    for dirpath, dirnames, filenames in os.walk(root_dir):
        rel_dir = os.path.relpath(dirpath, root_dir)
        if rel_dir == ".":
            rel_dir = ""
        else:
            summary += f"- {rel_dir}/\n"
        for f in filenames:
            summary += f"  - {f}\n"
    return summary

def update_readme(readme_path, summary):
    with open(readme_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("# Project\n\n")
        f.write(summary)

if __name__ == "__main__":
    root = "."  
    readme = "README.md"
    summary_text = generate_summary(root)
    update_readme(readme, summary_text)
    print("README.md อัปเดตเรียบร้อยแล้ว")
