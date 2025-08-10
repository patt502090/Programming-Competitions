import os
import urllib.parse

# โฟลเดอร์และไฟล์ที่ไม่ต้องการให้แสดง
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
    # ส่วนหัว README
    header = """# 🏆 Competitive Programming Archive

![Banner](https://via.placeholder.com/900x200/4B8BBE/FFFFFF?text=Competitive+Programming+Repo)

> 💻 รวมโค้ดเก่าๆ จากการฝึกเขียนโปรแกรมแข่งขัน เก็บไว้เป็นความทรงจำ และอ้างอิงในอนาคต
> 📅 ภาษา: **Python**, **Go**
> ✨ มีทั้งโจทย์จาก **ICPC**, **TOI**, **LeetCode**, **Codeforces** และอื่นๆ

---

## 📂 โครงสร้างโปรเจกต์
"""
    # สร้างรายการไฟล์แบบ Markdown
    lines = md_list(".")
    output = header + "\n".join(lines) + """

---

## 📊 สถิติภาษา
![Languages](https://img.shields.io/github/languages/top/USERNAME/REPO?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/USERNAME/REPO?color=green&style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/USERNAME/REPO?style=for-the-badge)

---

## 💡 วิธีใช้งาน
1. เปิดไฟล์ที่ต้องการศึกษา
2. อ่านโค้ดและลองรัน
3. ปรับปรุงต่อยอดได้ตามต้องการ

---

⭐ ถ้าชอบกด Star ให้กำลังใจด้วยนะ
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(output)
