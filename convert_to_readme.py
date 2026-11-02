import os
import re

PROBLEMS_DIR = "problems"

def parse_and_convert():
    if not os.path.exists(PROBLEMS_DIR):
        print(f"❌ 找不到 {PROBLEMS_DIR} 資料夾！")
        return

    count = 0
    for root, dirs, files in os.walk(PROBLEMS_DIR):
        if "solution.py" in files:
            sol_path = os.path.join(root, "solution.py")
            readme_path = os.path.join(root, "README.md")

            with open(sol_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 使用 Regex 提取多行字串 (題目敘述) 與底下的程式碼
            docstring_match = re.search(r'^\s*"""(.*?)"""(.*)$', content, re.DOTALL)

            if docstring_match:
                docstring = docstring_match.group(1).strip()
                code_body = docstring_match.group(2).strip()

                # 1. 建立 README.md 內容
                readme_content = f"# Problem Description\n\n```text\n{docstring}\n```\n\n## Solution\n\nSee [`solution.py`](./solution.py) for the implementation.\n"

                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write(readme_content)

                # 2. 清洗 solution.py（移除頂部的題目長字串，僅保留程式碼骨架）
                with open(sol_path, "w", encoding="utf-8") as f:
                    f.write(f"# Write your solution below\n\n{code_body}\n")

                count += 1
                print(f"✅ 已為 {os.path.basename(root)} 建立 README.md 並重構 solution.py")

    print(f"\n🎉 處理完成！共轉換/建立 {count} 個 README.md 檔案。")

if __name__ == "__main__":
    parse_and_convert()