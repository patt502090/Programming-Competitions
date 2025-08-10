import os
import urllib.parse

# Folders and files to ignore
IGNORE_DIRS = {'.git', '.cph', 'script_name.py', '__pycache__'}

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
            lines.append(f"{prefix}- 📁 **{entry}/**")
            lines.extend(md_list(full_path, prefix + "  "))
        else:
            rel_path = os.path.relpath(full_path, start=".").replace("\\", "/")
            rel_path = urllib.parse.quote(rel_path)
            lines.append(f'{prefix}- 📄 [{entry}]({rel_path})')
    return lines

if __name__ == "__main__":
    # README header
    header = """# 🏆 Competitive Programming Archive

![Banner](https://via.placeholder.com/900x200/4B8BBE/FFFFFF?text=Competitive+Programming+Repo)

> 💻 A collection of past code from competitive programming practice — kept as a memory and for future reference  
> 📅 Languages: **Python**, **Go**  
> ✨ Featuring problems from **ICPC**, **TOI**, **LeetCode**, **Codeforces**, and more

---

## 📂 Project Structure
"""
    # Generate Markdown file tree
    lines = md_list(".")
    output = header + "\n".join(lines) + """

---

## 📊 Repository Stats
![Languages](https://img.shields.io/github/languages/top/patt502090/REPO?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/patt502090/REPO?color=green&style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/patt502090/REPO?style=for-the-badge)

---

## 💡 How to Use
1. Open the file you want to explore
2. Read the code and try running it
3. Improve, modify, and experiment as you like

---

⭐ If you enjoy this repo, consider giving it a Star!
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(output)
