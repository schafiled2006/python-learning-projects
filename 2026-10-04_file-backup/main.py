import shutil
import time
import os

SOURCE = "notes"
BACKUPS = "backups"

def backup_folder():
    if not os.path.isdir(SOURCE):
        print("nothing to back up, folder", SOURCE, "missing")
        return
    stamp = time.strftime("%Y%m%d-%H%M%S")
    dest = os.path.join(BACKUPS, stamp)
    shutil.copytree(SOURCE, dest)
    print("backup saved to", dest)

def prune(keep=5):
    runs = sorted(os.listdir(BACKUPS))
    for old in runs[:-keep]:
        shutil.rmtree(os.path.join(BACKUPS, old))
        print("pruned", old)

backup_folder()
prune()
