# -*-coding: utf-8 -*-

from subprocess import call

def main():
    basepath = "../data/2251/"
    
    for i in range(1, 10):
        filename = "data.txt"
        path = basepath + str(i) + "/" + filename
        
        # call(["python", "crude_values.py", path])
        # call(["python", "moving_average.py", path, "1", "7"])

if __name__ == "__main__":
    main()
