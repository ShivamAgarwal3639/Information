# Essential Git Commands - Tabular Reference

## 1. Initial Setup & Configuration

| Command | Purpose | Example |
|---------|---------|---------|
| `git config` | Set identity | `git config --global user.name "Your Name"` |
| | | `git config --global user.email "your.email@company.com"` |
| `git clone` | Copy repository | `git clone <repository-url>` |
| `git remote -v` | Check remote URLs | `git remote -v` |

## 2. Branching Workflow

| Command | Purpose | Example |
|---------|---------|---------|
| `git checkout -b` | Create and switch to new branch | `git checkout -b feature/new-feature` |
| `git switch -c` | Create and switch to new branch (modern) | `git switch -c feature/new-feature` |
| `git branch -a` | List all branches | `git branch -a` |
| `git checkout` | Switch to existing branch | `git checkout main` |
| `git switch` | Switch to existing branch (modern) | `git switch main` |
| `git branch -d` | Delete a merged branch | `git branch -d old-branch` |
| `git checkout --track` | Track a remote branch locally | `git checkout --track origin/remote-branch` |

## 3. Daily Workflow (Code Changes)

| Command | Purpose | Example |
|---------|---------|---------|
| `git status` | Check status of changes | `git status` |
| `git add` | Stage specific files | `git add file1.js file2.js` |
| `git add .` | Stage all changes | `git add .` |
| `git commit` | Commit changes | `git commit -m "Descriptive commit message"` |
| `git push` | Push to remote branch | `git push origin feature/new-feature` |
| `git pull` | Pull latest changes | `git pull` |

## 4. Collaboration & Syncing

| Command | Purpose | Example |
|---------|---------|---------|
| `git fetch` | Fetch remote changes without merging | `git fetch origin` |
| `git merge` | Merge changes from another branch | `git merge main` |
| `git rebase` | Rebase your branch | `git rebase main` |
| `git add .` | Mark conflicts as resolved | `git add .` |
| `git rebase --continue` | Continue rebase after resolving conflicts | `git rebase --continue` |
| `git merge --continue` | Continue merge after resolving conflicts | `git merge --continue` |

## 5. Undoing Mistakes

| Command | Purpose | Example |
|---------|---------|---------|
| `git restore` | Undo unstaged changes | `git restore file.js` |
| `git restore --staged` | Unstage a file (keep changes) | `git restore --staged file.js` |
| `git commit --amend` | Amend the last commit | `git commit --amend` |
| `git reset --hard` | Reset to a previous commit | `git reset --hard HEAD~1` |
| `git revert` | Revert a commit | `git revert <commit-hash>` |
| `git stash` | Temporarily save work | `git stash` |
| `git stash pop` | Restore stashed changes | `git stash pop` |

## 6. Advanced Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `git log` | View commit history | `git log --oneline --graph` |
| `git diff` | Compare working vs. staged | `git diff` |
| `git diff --staged` | Compare staged vs. committed | `git diff --staged` |
| `git blame` | Check who changed a line | `git blame file.js` |
| `git clean` | Clean untracked files | `git clean -df` |
| `git reflog` | Find lost commit hash | `git reflog` |
| `git reset --hard <hash>` | Recover lost commits | `git reset --hard <hash>` |

## 7. Working with Remote Repositories

| Command | Purpose | Example |
|---------|---------|---------|
| `git remote add` | Add a new remote | `git remote add upstream <url>` |
| `git push --force` | Force push (use cautiously) | `git push origin feature/new-feature --force` |
| `git fetch --prune` | Prune stale branches | `git fetch --prune` |

## 8. Troubleshooting

| Command | Purpose | Example |
|---------|---------|---------|
| `git diff` | Identify conflicts | `git diff` |
| `git reset --hard HEAD~1` | Undo accidental commit to main | `git reset --hard HEAD~1` |
| `git switch -c temp-branch` | Fix detached HEAD state | `git switch -c temp-branch` |
