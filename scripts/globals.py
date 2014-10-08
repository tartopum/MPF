# -*-coding: utf-8 -*-

import glob
import os.path
import sys
import numpy as np
import matplotlib.pyplot as plt

def draw(x, y, filename, title=""):    
    plt.plot(x, y)
    plt.xlabel("Days")
    plt.ylabel("Production (L)")
    plt.title(title)
    plt.grid(True)
    
    ymin = min(y)
    ymax = max(y)
    plt.ylim([ymin - 2, ymax + 2])
    
    plt.savefig(filename + ".png")

def get_filename(path, suffix="", prefix=""):
    return prefix + os.path.splitext(path)[0] + suffix

def get_filenames(folder):
    for root, dirnames, filenames in os.walk(folder):
        print os.path.join(folder, filenames)
    
def get_values(f):
    x = []
    y = []
    
    for line in f.readlines():
            x_value, y_value = line.strip().split(" ")
            y_value = round(float(y_value.replace(",", ".")), 2)
            
            x.append(int(x_value))
            y.append(y_value)
            
    return x, y

if __name__ == "__main__":
    print get_filenames(sys.argv[1])
