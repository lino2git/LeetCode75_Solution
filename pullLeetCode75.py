import requests
import json
import os
import re
import time

URL = "https://leetcode.com/graphql"

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://leetcode.com/studyplan/leetcode-75/",
    "Origin": "https://leetcode.com"
}

# 1. 取得 LeetCode 75 題目清單
QUERY_PLAN = """
query studyPlanV2Detail($planSlug: String!) {
  studyPlanV2Detail(planSlug: $planSlug) {
    planSubGroups {
      slug
      name
      questions {
        questionFrontendId
        title
        titleSlug
        difficulty
      }
    }
  }
}
"""

# 2. 依據 titleSlug 取得單一題目的內容 (Description + Code Snippet)
QUERY_QUESTION = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    content
    codeSnippets {
      lang
      langSlug
      code
    }
  }
}
"""

def html_to_clean_text(html_content):
    """簡單將 LeetCode 的 HTML 題目內容轉成乾淨的文字與註解"""
    if not html_content:
        return ""
    # 替換常見 HTML 標籤
    text = re.sub(r'</?p>', '\n', html_content)
    text = re.sub(r'</?ul>', '\n', text)
    text = re.sub(r'<li>', '- ', text)
    text = re.sub(r'</li>', '\n', text)
    text = re.sub(r'<code>', '`', text)
    text = re.sub(r'</code>', '`', text)
    text = re.sub(r'<pre>', '\n```\n', text)
    text = re.sub(r'</pre>', '\n```\n', text)
    text = re.sub(r'<[^>]+>', '', text) # 清除其餘標籤
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&lt;', '<', text)
    text = re.sub(r'&gt;', '>', text)
    text = re.sub(r'&quot;', '"', text)
    return text.strip()

def fetch_leetcode_75():
    response = requests.post(
        URL, 
        json={"query": QUERY_PLAN, "variables": {"planSlug": "leetcode-75"}}, 
        headers=HEADERS
    )
    if response.status_code != 200:
        print(f"Failed to fetch study plan: {response.status_code}")
        return []

    res_data = response.json()
    subgroups = res_data.get("data", {}).get("studyPlanV2Detail", {}).get("planSubGroups", [])
    
    questions = []
    for group in subgroups:
        category = group['name']
        for q in group['questions']:
            q['category'] = category
            questions.append(q)
    return questions

def fetch_question_detail(title_slug):
    response = requests.post(
        URL, 
        json={"query": QUERY_QUESTION, "variables": {"titleSlug": title_slug}}, 
        headers=HEADERS
    )
    if response.status_code == 200:
        return response.json().get("data", {}).get("question", {})
    return None

def main():
    questions = fetch_leetcode_75()
    print(f"共找到 {len(questions)} 道題目，準備開始建立檔案與抓取題目內容...\n")

    for idx, q in enumerate(questions, start=1):
        q_id = q['questionFrontendId'].zfill(4) # 補齊 4 位數，方便排序 (例如 0001)
        slug = q['titleSlug']
        category_dir = os.path.join("problems", q['category'].lower().replace(" ", "_"))
        prob_dir = os.path.join(category_dir, f"p{q_id}_{slug.replace('-', '_')}")
        
        os.makedirs(prob_dir, exist_ok=True)
        
        sol_path = os.path.join(prob_dir, "solution.py")
        
        # 避免重複抓取已經建立過的檔案
        if os.path.exists(sol_path):
            print(f"[{idx}/{len(questions)}] 跳過 (已存在): {q['title']}")
            continue

        print(f"[{idx}/{len(questions)}] 正在抓取詳細內容: [{q['questionFrontendId']}] {q['title']}...")
        detail = fetch_question_detail(slug)
        
        if not detail:
            print(f"  ❌ 抓取失敗: {slug}")
            continue

        # 1. 處理題目敘述
        description = html_to_clean_text(detail.get("content", ""))

        # 2. 抓取 Python 3 的 Code Snippet 骨架
        py3_code = ""
        snippets = detail.get("codeSnippets", []) or []
        for snippet in snippets:
            if snippet.get("langSlug") == "python3":
                py3_code = snippet.get("code", "")
                break

        if not py3_code:
            py3_code = "class Solution:\n    pass\n"

        # 3. 寫入 solution.py
        with open(sol_path, "w", encoding="utf-8") as f:
            f.write(f'"""\n')
            f.write(f'LeetCode {q["questionFrontendId"]}: {q["title"]}\n')
            f.write(f'Category: {q["category"]}\n')
            f.write(f'Difficulty: {q["difficulty"]}\n')
            f.write(f'URL: https://leetcode.com/problems/{slug}/\n\n')
            f.write(f'=== Description ===\n')
            f.write(f'{description}\n')
            f.write(f'"""\n\n')
            f.write(f'# Write your solution below\n')
            f.write(py3_code)
            f.write("\n")

        # 適度暫停，避免請求過於頻繁被 LeetCode 限流
        time.sleep(0.5)

    print("\n🎉 全部題目與敘述已成功下載並建立完成！")

if __name__ == "__main__":
    main()