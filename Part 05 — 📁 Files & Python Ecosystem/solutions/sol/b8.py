# # ⚔️ Mini Challenge — The Dependency Detective
# Read this situation.
# ```text
# You have two projects.

# Project A:

# Needs:
# pandas
# numpy
# matplotlib


# Project B:

# Needs:
# fastapi
# requests
# ```

# Answer these questions:

# ### 1. Should both projects share one virtual environment?

# Explain why or why not.
# Ans=> The two projects need different packages or have different dependencies so it's better to keep them in their on virtual environments. It's alot a lot cleaner that way.
# ---

# ### 2. Where should you install Project A's packages?

# ```text
# Global Python?

# or

# Project A's environment?
# ```
# Ans=> Project A's environment

# ---

# ### 3. What happens if Project B needs a different version of `requests` than another project?
# Ans=> Project B should be in its own virtual environment so it can safely install its own required version of the 'requests' package. This way, another project using a different 'requests' package version doesn't break.
# ---

# ### 4. Complete the architecture:

# ```text
# Project A
#     │
#     └── __________________
#             │
#             ├── pandas
#             ├── numpy
#             └── matplotlib


# Project B
#     │
#     └── __________________
#             │
#             ├── fastapi
#             └── requests
# ```
# Ans=>
# ```text
# Project A
#     │
#     └── main.py
#     │
#     └──venv 
#           │
#           └── other venv related files/folder
#             │──installed packages
#             │
#             ├── pandas
#             ├── numpy
#             └── matplotlib

# Project B
#     │
#     └── main.py
#     │
#     └──venv 
#           │
#           └── other venv related files/folder
#             │──installed packages
#             │
#             ├── fastapi
#             ├── requests