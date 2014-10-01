# -*-coding: utf-8 -*-

import os.path
import sys
import numpy as np
import matplotlib.pyplot as plt

def main(args):
    path = args[0]
    with open(path, "r") as f:
        days = []
        amounts = []
        for line in f.readlines():
            day, amount = line.strip().split(" ")
            amount = round(float(amount.replace(",", ".")), 2)
            
            days.append(int(day))
            amounts.append(amount)
    
    filename = os.path.splitext(path)[0]
    
    plt.plot(days, amounts)
    plt.xlabel("Jours")
    plt.ylabel("Production (L)")
    plt.grid(True)
    
    ymin = min(amounts)
    ymax = max(amounts)
    plt.ylim([ymin - 2, ymax + 2])
    plt.savefig(filename + ".png")
    
if __name__ == "__main__":
    main(sys.argv[1:])
