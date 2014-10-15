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
    
    plt.ylim([0, 40])
    
    ensure_dir(filename)
    plt.savefig(filename + ".png")

def ensure_dir(path):
    d = os.path.dirname(path)
    if not(os.path.exists(d)):
        os.makedirs(d)

def get_filename(path, name):
    return os.path.join(os.path.dirname(os.path.splitext(path)[0]), name)

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
