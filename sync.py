import requests
import os
import json
from datetime import datetime
from pathlib import Path

USERNAME = "Sjain98"
COOKIE = os.environ.get("LEETCODE_SESSION")

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": f"LEETCODE_SESSION={COOKIE}"
}

GRAPHQL_URL = "https://leetcode.com/graphql"

RECENT_SUBMISSION_QUERY = """
query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    title
    titleSlug
    timestamp
  }
}
"""

QUESTION_DETAIL_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    title
    difficulty
    content
    codeSnippets {
      lang
      code
    }
  }
}
"""

def fetch_recent_submissions():
    variables = {"username": USERNAME, "limit": 10}
    r = requests.post(GRAPHQL_URL, json={"query": RECENT_SUBMISSION_QUERY, "variables": variables}, headers=HEADERS)
    return r.json()["data"]["recentAcSubmissionList"]

def fetch_question_detail(slug):
    r = requests.post(GRAPHQL_URL, json={"query": QUESTION_DETAIL_QUERY, "variables": {"titleSlug": slug}}, headers=HEADERS)
    return r.json()["data"]["question"]

def sanitize_filename(name):
    return "".join(c if c.isalnum() or c in "_-" else "_" for c in name)

def save_question(q):
    title = q["title"]
    qid = q["questionId"].zfill(4)
    slug = sanitize_filename(q["title"])
    difficulty = q["difficulty"].lower()
    content = q["content"]
    code = next((s["code"] for s in q["codeSnippets"] if s["lang"] == "Python3"), None)

    if not code:
        return

    folder = Path(difficulty)
    folder.mkdir(exist_ok=True)

    filename = f"{qid}_{slug}.py"
    filepath = folder / filename

    if filepath.exists():
        return

    with open(filepath, "w", encoding="utf-8") as f:
        f.write('"""\n')
        f.write(content.replace("<br>", "\n").replace("</p>", "\n").replace("<p>", "").replace("\r", "").replace("&nbsp;", " "))
        f.write('\n"""\n\n')
        f.write(code)

    print(f"✅ Saved: {filepath}")

def main():
    submissions = fetch_recent_submissions()
    for sub in submissions:
        detail = fetch_question_detail(sub["titleSlug"])
        save_question(detail)

if __name__ == "__main__":
    main()
