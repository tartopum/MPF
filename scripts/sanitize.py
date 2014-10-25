# -*-coding: utf-8 -*-

import sys

def sanitize_line(line):
    line = line.strip()
    line = line.replace("\t", " ")
    return line

def main(args):
    path = args[0]
    
    with open(path, "r") as f:
        lines = f.readlines()
        
    with open(path, "w") as f:    
        lines = lines[2:]
        lines = map(sanitize_line, lines)
        lines = [line for line in lines if line != ""]
        
        txt = "\n".join(lines)
        
        f.write(txt)

if __name__ == "__main__":
    main(sys.argv[1:])
