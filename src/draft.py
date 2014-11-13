import os
from subprocess import call

basename = os.path.basename
dirname = os.path.dirname
join = os.path.join
normpath = os.path.normpath
splitext = os.path.splitext

def sanitize(line):
    return line.replace(",", ".")

for root, subdirs, files in os.walk("../data/"):
    for f in files:	
        path = join(root, f)
        
        if "csv" in path:
            with open(path, "r") as f:
                lines = f.readlines()
                lines = list(map(sanitize, lines))
                
            with open(path, "w") as f:
                f.write("".join(lines))
