import subprocess
import sys
from datetime import datetime, timedelta

def git_status(git_dir):
    
    # Get the active branch
    branch = subprocess.check_output(['git', '-C', git_dir, 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')
    print("active branch:", branch)

    # Check for local changes
    changes = subprocess.run(['git', '-C', git_dir, 'diff-index', 'HEAD'], capture_output=True, text=True)
    if changes.stdout:
        print("local changes: True")
    else:
        print("local changes: False")

    # Check the date of the last commit
    date = subprocess.check_output(['git', '-C', git_dir, 'log', '-1', '--format=%ci']).strip().decode('utf-8')
    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S %z')
    
    if date.date() >= datetime.now().date() - timedelta(days=7):
        print("recent commit: True")
    else:
        print("recent commit: False")

    # Check the author of the last commit
    author = subprocess.check_output(['git', '-C', git_dir, 'log', '-1', '--format=%an']).strip().decode('utf-8')
    if author == "Rufus":
        print("blame Rufus: True")
    else:
        print("blame Rufus: False")

# git_dir is the argument that is provided in the command prompt
git_dir = sys.argv[1]
git_status(git_dir)