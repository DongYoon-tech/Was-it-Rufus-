# Git Status Checker

A script that provides information about the current state of a git repository.

## Requirements
- Python
- Git

## How to Run
1. Open your command prompt/terminal and navigate to the directory where the script is located.
2. Run the script by typing in `python app.py` followed by the path of the git directory you want to check.
   - Example: `python app.py C:\Users\Desktop\Project`
3. The script will execute and provide you with the following information:
   - Active branch: the current branch you are on in the git repository
   - Local changes: whether or not there are any changes that have not been committed
   - Recent commit: whether or not the last commit was made within the last 7 days
   - Blame Rufus: whether or not the last commit was made by a user named Rufus
4. Please ensure that the script has the correct path of the git repository and that you have git installed in your system, otherwise the script will throw an error.
