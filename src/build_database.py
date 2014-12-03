from os import remove
from os.path import join, isfile
import subprocess
from config import DATABASE_PATH, SQL_PATH

print(DATABASE_PATH)

if isfile(DATABASE_PATH):
    remove(DATABASE_PATH)

print("Building database...")
print("Building tables...")

cat = subprocess.Popen(["cat", join(SQL_PATH, "tables.sql")], stdout=subprocess.PIPE)
sql = subprocess.Popen(["sqlite3", DATABASE_PATH], stdin=cat.stdout)
cat.stdout.close()

print("Database initialized successfully.")
