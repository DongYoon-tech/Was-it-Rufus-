import sys
import subprocess
from datetime import datetime, timedelta

def git_status(git_dir):
    
    # Get the active branch
    active_branch = subprocess.check_output(['git', '-C', git_dir, 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')
    print("active branch:", active_branch)

    # Check for local changes
    local_changes = subprocess.run(['git', '-C', git_dir, 'diff-index', 'HEAD'], capture_output=True, text=True)
    if local_changes.stdout:
        print("local changes: True")
    else:
        print("local changes: False")

    # Check the date of the last commit
    date = subprocess.check_output(['git', '-C', git_dir, 'log', '-1', '--format=%ci']).strip().decode('utf-8')
    last_commit_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S %z')
    today_date = datetime.now().date() - timedelta(days=7)
    
    # Check if the last commit was made within the last 7 days
    if last_commit_date.date() >= today_date:
        print("recent commit: True")
    else:
        print("recent commit: False")

    # Check the author of the last commit
    author = subprocess.check_output(['git', '-C', git_dir, 'log', '-1', '--format=%an']).strip().decode('utf-8')
    if author == "Rufus":
        print("blame Rufus: True")
    else:
        print("blame Rufus: False")

# git_dir is the command input
git_dir = sys.argv[1]
git_status(git_dir)