import os
from subprocess import call

basename = os.path.basename
dirname = os.path.dirname
join = os.path.join
normpath = os.path.normpath

for root, subdirs, files in os.walk("../data/"):
    for f in files:	
        path = join(root, f)
        try:		
            d = int(dirname(path)[-1])
        except:
            d = -1
		
        if d > -1 and "data.txt" in path:
            dest = join(dirname(path), "..")
            dest = normpath(dest)
            dest = join(dest, str(d) + ".csv")

            call(["cp", path, dest])
