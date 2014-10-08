# -*-coding: utf-8 -*-

import os.path
import sys
from globals import draw, get_filename, get_values

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
         
    filename = os.path.splitext(path)[0] + ".moving-average_" + str(count) + "_" + str(n)
    draw(days, amounts, filename, "Moving average " + str(count) + " " + str(n))

if __name__ == "__main__":
    main(sys.argv[1:])
