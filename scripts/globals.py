# -*-coding: utf-8 -*-

import os
from path import path
import re
import numpy as np
import matplotlib.pyplot as plt

def draw(filename, title="", xlabel="Days", ylabel="Production (L)"):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    
    if title == "":
        title = "/".join(split_filename(filename))
        plt.title(title)
    
    ensure_dir(filename)
    plt.savefig(filename + ".png")
    plt.clf()

def ensure_dir(path):
    d = os.path.dirname(path)
    if not(os.path.exists(d)):
        os.makedirs(d)

def get_filename(path, name):
    return os.path.join(os.path.dirname(os.path.splitext(path)[0]), name)

def get_filenames():
    return [filename for filename in path("../data/").walkfiles()]

def get_graph_names():
    num = get_numeros()[0]
    folder = os.listdir("../data/" + num)[0]
    path_ = "../data/" + num + "/" + folder
    
    return [os.path.basename(f) for f in path(path_).walkfiles() if ".png" in f]

def get_numeros():
    return os.listdir("../data")
    
def get_values(f):
    x = []
    y = []
    
    for line in f.readlines():
        x_value, y_value = line.strip().split(" ")
        y_value = round(float(y_value.replace(",", ".")), 2)
            
        x.append(int(x_value))
        y.append(y_value)
            
    return x, y

def split_filename(filename):
    search = re.search(".+/data/([0-9]+)/([0-9]+)/(.+)$", filename)
    return search.group(1), search.group(2), search.group(3)     

