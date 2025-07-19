# LeetCode Sync Bot

Automatically syncs accepted LeetCode submissions to this GitHub repository every day.

## How it works

This repo is powered by a GitHub Actions workflow that:

1. Logs into LeetCode account using a session token.
2. Pulls 10 most recent accepted submissions.
3. Saves them into folders based on difficulty (`easy/`, `medium/`, `hard/`).
4. Includes full problem description and Python solution.
5. Updates this README to include a running list of solved problems.
