# Simple file backup/copy program. Customize your own "BACKUP_FILES & BACKUP_DIRECTORY".
import datetime
import os
import shutil

BACKUP_FILES = '/Users/me/test' 
BACKUP_DIRECTORY = '/Users/me/test/main/qb_backup_{0}'

def get_backup_directory(base_directory):
    date = datetime.datetime.now().strftime('%Y-%m-%d-%H%M-%a')
    return base_directory.format(date)

def copy_files(BACKUP_FILES, BACKUP_DIRECTORY, symlinks=False, ignore=None):
    for item in os.listdir(BACKUP_FILES):
        s = os.path.join(BACKUP_FILES, item)
        d = os.path.join(BACKUP_DIRECTORY, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def perform_backup(base_directory):
    backup_directory = get_backup_directory(base_directory)
    os.makedirs(backup_directory)
    copy_files(BACKUP_FILES, backup_directory)

def main():
    perform_backup(BACKUP_DIRECTORY)

if __name__ == '__main__':
    main()

raw_input("Press enter to exit ;)")
