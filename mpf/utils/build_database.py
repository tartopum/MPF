import sys
from os import remove
from os.path import dirname, join, isfile, realpath
import subprocess

from mpf.config import DATABASE_PATH, DATABASE_DIR




def query_yes_no(question, default="yes"):
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

                             
if isfile(DATABASE_PATH):
    if query_yes_no("Delete the current database?", default="no"):
        remove(DATABASE_PATH)

print("Building database...")
print("Building tables...")

cat = subprocess.Popen(["cat", join(DATABASE_DIR, "tables.sql")], stdout=subprocess.PIPE)
sql = subprocess.Popen(["sqlite3", DATABASE_PATH], stdin=cat.stdout)
cat.stdout.close()

print("Database initialized successfully.")
