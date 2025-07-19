import os
from pathlib import Path

README_PATH = "README.md"

def generate_readme():
    rows = []
    rows.append("| # | Title | Difficulty | Link |")
    rows.append("|:-:|-------|:----------:|------|")

    for difficulty in ["easy", "medium", "hard"]:
        dir_path = Path(difficulty)
        if not dir_path.exists():
            continue

        for file in sorted(dir_path.glob("*.py")):
            filename = file.name
            if "_" not in filename:
                continue

            number, *title_parts = filename.replace(".py", "").split("_")
            title = " ".join(title_parts).capitalize()
            url = f"{difficulty}/{filename}"
            rows.append(f"| {int(number)} | {title} | {difficulty.title()} | [{filename}]({url}) |")

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write("# LeetCode Solutions\n\n")
        f.write("Automatically synced from LeetCode using GitHub Actions.\n\n")
        f.write("\n".join(rows))

    print("README updated.")

if __name__ == "__main__":
    generate_readme()
