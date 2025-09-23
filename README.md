# GitHub CheatCode

> **Transform your GitHub profile from ghost to "active" developer in 30 seconds**

This project demonstrates the absurdity of using GitHub activity as a recruitment criterion. In just a few clicks, go from 0 to 365+ contributions.

## Why this project?

"Not active enough on GitHub" = Red flag for some recruiters?

This project proves that these metrics are **totally artificial** and can be manipulated in just a few minutes. GitHub activity doesn't reflect a developer's real skills at all.

## Quick installation

### Option 1: Instant fill (365 days in 30 seconds)

```bash
# 1. Clone this repo
git clone https://github.com/YOUR_USERNAME/github-cheatcode.git
cd github-cheatcode

# 2. Initialize git
git init

# 3. Run the magic script
python3 github-cheatcode.py

# 4. Create a new repo on GitHub and push
git remote add origin https://github.com/YOUR_USERNAME/my-awesome-project.git
git branch -M main
git push -u origin main --force
```

**Result:** Your profile instantly displays 365+ days of contributions!

### Option 2: Daily automatic commits (GitHub Actions)

Once the repo is pushed to GitHub, commits are made automatically every day at 2 PM UTC thanks to GitHub Actions.

**That's it!** No additional configuration, 100% free.

## Features

- **Instant fill**: 365 days of history in a few seconds
- **Automatic commits**: 1 commit per day via GitHub Actions
- **Varied messages**: Commits look natural
- **Realistic pattern**: Fewer commits on weekends and in August
- **100% Free**: No server, no cost

## How it works

1. **Python Script**: Rewrites Git history with dates in the past
2. **GitHub Actions**: Workflow that runs daily
3. **Counter.txt**: Simple file incremented with each commit

## Customization

### Modify daily commit frequency

Edit `.github/workflows/daily-commit.yml`:

```yaml
schedule:
  - cron: "0 14 * * *" # Every day at 2 PM UTC
```

### Add more commits per day

Duplicate the cron line with different hours:

```yaml
schedule:
  - cron: "0 9 * * *" # 9 AM UTC
  - cron: "0 14 * * *" # 2 PM UTC
  - cron: "0 19 * * *" # 7 PM UTC
```

---

**PS:** If a recruiter reads this, I hope you'll judge candidates on their real skills, not on green squares.

**PPS:** For developers: your value isn't measured in commits. Some of the best developers I know have almost empty GitHubs because they work on proprietary code.
