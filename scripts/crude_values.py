# -*-coding: utf-8 -*-

import os.path
import sys
import numpy as np
import matplotlib.pyplot as plt
from globals import draw, ensure_dir, get_filename, get_values

def main(args):
    path = args[0]
    with open(path, "r") as f:
        days, amounts = get_values(f)
    
    filename = get_filename(path, "crude-values")
    title = filename
    plt.plot(days, amounts)
    plt.ylim([0, max(40, max(amounts))])
    draw(filename, title=title)
    
if __name__ == "__main__":
    main(sys.argv[1:])
