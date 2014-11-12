import sys
import numpy as np
import matplotlib.pyplot as plt
from globals import get_values

def get_a_b(x, y):  
    x_average = sum(x)/len(x)
    y_average = sum(y)/len(y)
    
    a_num = 0
    a_den = 0
    for i in range(len(x)):
        a_num += (x[i] - x_average) * (y[i] - y_average)
        a_den += (x[i] - x_average)**2
    
    a = a_num/a_den
    b = y_average - a * x_average
    
    return a, b
    

def main(args):
    path = args[0]
    with open(path, "r") as f:
        days, amounts = get_values(f)
    
    plt.plot(days, amounts)
    
    threshold = 50
    
    # Rising during 50 days
    rising_days = days[:threshold]
    rising_amounts = amounts[:threshold]
    
    a, b = get_a_b(rising_days, rising_amounts)
    
    x = np.array(rising_days)
    plt.plot(x, a*x + b, "r", lw=2)
    
    # Then falling
    falling_days = days[threshold:]
    falling_amounts = amounts[threshold:]
    
    a, b = get_a_b(falling_days, falling_amounts)
    
    x = np.array(falling_days)
    plt.plot(x, a*x + b, "r", lw=2)  
    plt.show()
    
    # filename = get_filename(path, "least-squares")
    # draw(filename, xlabel="Days", ylabel="Production (L)")
    

if __name__ == "__main__":
    main(sys.argv[1:])
