# # 🥋 Skill Check
# Answer these without looking back if you can.

# ### 1. What problem does Git solve?
# ANS => As a version control system, it helps to track changes made in a project eliminating the need for making various copies of same project as it grows or more features are added. It also help with organisation as well.
# ---

# ### 2. What is a commit?
# ANS => A commit is a more of a checkpoint that defines what changes you've made in a project
# ---

# ### 3. What does this command do?
# ```bash
# git status
# ```
# Ans => It shows whats being tracked by git
# Correction > 🐛 Slightly off. git status doesn't just show what's being tracked — it shows the current state of your working directory and staging area: which files are modified, which are staged, and which are untracked (new, not yet added). "What's being tracked" undersells it — it's more like a live diff-status report.
# ---


# ### 4. What is the staging area?
# Ans =>  This shows the files being tracked by git
# Correction => This is mixed up with git status's job. The staging area isn't something that "shows" you anything — it's a physical holding zone. It's where you place the specific changes you want included in your next commit, separate from your full working directory. Think of it as a prep table before you package (commit) the changes.
# ---

# ### 5. What does this do?
# ```bash
# git add main.py
# ```
# Ans => It adds tracked files to the staging area 

# ---

# ### 6. What does this do?
# ```bash
# git commit -m "Add player class"
# ```
# Ans => Idetifies or tracks the change made in the project and calls this stage or checkpoint "Add player class" for reference.
# Correction => Minor imprecision: git commit -m "..." doesn't "identify/track" changes — that's staging's job. A commit takes whatever is currently staged and saves it as a permanent snapshot in the repo's history, labeled with your message.
# ---

# ### 7. Why would you usually add this to `.gitignore`?
# ```text
# venv/
# ```
# Ans => It can be reproduced and usually contain unimportant files we don't want to track.

# ---

# ### 8. Complete the flow:
# ```text
# Working Directory
#         │
#         │ __________
#         ▼
# Staging Area
#         │
#         │ __________
#         ▼
# Repository
# Ans =>
# ```text
# Working Directory
#         │
#         │ __________All my files and folder
#         ▼
# Staging Area
#         │
#         │ __________Only what i want to track
#         ▼
# Repository
# Correction => The blanks were asking for the commands that move you between stages, not descriptions of what each stage contains. What command moves files from Working Directory → Staging Area? What command moves from Staging Area → Repository? (You've literally answered both of these correctly in Q5 and Q6 — just plug those commands into the diagram.)
# ```