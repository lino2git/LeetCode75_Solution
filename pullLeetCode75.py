import requests
import json

url = "https://leetcode.com/graphql"

# 更新後的 V2 Query
query = """
query studyPlanV2Detail($planSlug: String!) {
  studyPlanV2Detail(planSlug: $planSlug) {
    planSubGroups {
      slug
      name
      questions {
        id
        questionFrontendId
        title
        titleSlug
        difficulty
      }
    }
  }
}
"""

variables = {
    "planSlug": "leetcode-75"
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://leetcode.com/studyplan/leetcode-75/",
    "Origin": "https://leetcode.com"
}

response = requests.post(
    url, 
    json={"query": query, "variables": variables}, 
    headers=headers
)

if response.status_code == 200:
    res_data = response.json()
    if "errors" in res_data:
        print("GraphQL 返回錯誤：", res_data["errors"])
    else:
        plan_detail = res_data.get("data", {}).get("studyPlanV2Detail", {})
        subgroups = plan_detail.get("planSubGroups", [])
        
        total_count = 0
        for group in subgroups:
            print(f"\n=== Category: {group['name']} ===")
            for q in group["questions"]:
                total_count += 1
                print(f"[{q['questionFrontendId']}] {q['title']} ({q['difficulty']}) -> {q['titleSlug']}")
        
        print(f"\n成功取得 {total_count} 題資訊！")
else:
    print(f"Failed with status code: {response.status_code}")
    print("Response text:", response.text)