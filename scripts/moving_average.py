# -*-coding: utf-8 -*-

import os.path
import sys
import matplotlib.pyplot as plt
from globals import draw, ensure_dir, get_filename, get_values

def average(amounts, n):
    amounts_average = []
    
    for i in range(n, len(amounts)-n):
        s = sum(amounts[i-n:i+n+1])
        average = float(s) / (2 * n + 1)
        amounts_average.append(average)   
            
    return amounts_average

def main(args):
    path = args[0]
    with open(path, "r") as f:
        days, amounts = get_values(f)
    
    try:
        count = args[1]
    except IndexError:
        count = 1
    else:
        count = int(count)
        
    try:
        n = args[2]
    except IndexError:
        n = 1
    else:
        n = int(n)
    
    for i in range(count):
        days = days[n:len(days)-n]     
        amounts = average(amounts, n)
     
    filename = get_filename(path, "moving-average_" + str(count) + "x_" + str(n))
    plt.plot(days, amounts)
    plt.ylim([0, max(40, max(amounts))])
    draw(filename)

if __name__ == "__main__":
    main(sys.argv[1:])
