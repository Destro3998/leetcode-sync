import requests
import os
import json
from datetime import datetime
from pathlib import Path

USERNAME = "Sjain98"
COOKIE = os.environ.get("LEETCODE_SESSION")

headers = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": f"LEETCODE_SESSION={COOKIE}"
}

GRAPHQL_URL = "https://leetcode.com/graphql"

QUERY = """
query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    title
    titleSlug
    timestamp
  }
}
"""

def get_description(title_slug):
    query = {
        "query": """
        query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            title
            difficulty
            content
            codeSnippets {
              lang
              code
            }
          }
        }
        """,
        "variables": {"titleSlug": title_slug}
    }
    r = requests.post(GRAPHQL_URL, json=query, headers=headers)
    return r.json()["data"]["question"]

def save_file(q):
    title = q["title"]
    slug = title.replace(" ", "_").replace("-", "_")
    difficulty = q["difficulty"].lower()
    description = q["content"]
    code = next(s["code"] for s in q["codeSnippets"] if s["lang"] == "Python3")

    Path(difficulty).mkdir(exist_ok=True)

    filename = f"{slug}.py"
    path = os.path.join(difficulty, filename)

    if os.path.exists(path):
        return 

    with open(path, "w", encoding="utf-8") as f:
        f.write('"""\n')
        f.write(description.replace("\r\n", "\n").replace("<br>", "\n").replace("</p>", "\n"))
        f.write('\n"""\n\n')
        f.write(code)

    print(f"✅ Saved: {path}")

def main():
    payload = {
        "query": QUERY,
        "variables": {"username": USERNAME, "limit": 10}
    }
    r = requests.post(GRAPHQL_URL, json=payload, headers=headers)
    subs = r.json()["data"]["recentAcSubmissionList"]

    for sub in subs:
        q = get_description(sub["titleSlug"])
        save_file(q)

if __name__ == "__main__":
    main()
