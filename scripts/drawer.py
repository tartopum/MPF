from math import sqrt, ceil
import matplotlib.pyplot as plt

def draw(x, y, title, xlabel, ylabel):
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.title(title)

def save(x, y, dest, title="", xlabel="x", ylabel="y"):
    draw(x, y, title, xlabel, ylabel)
    plt.savefig(dest)
    plt.clf()

def show(x, y, title="", xlabel="x", ylabel="y"):
    draw(x, y, title, xlabel, ylabel)
    plt.show()
    plt.clf()
    

def gallery(x_list, y_list, titles):
    l = len(x_list)
    
    if titles == []:
        titles = ["" for i in range(l)]
    
    n = int(ceil(sqrt(l)))
    
    if n <= 1:
        draw(x_list[0], y_list[0], titles[0], "x", "y")
        return
    
    f, axarr = plt.subplots(n, n)
    
    for k in range(l):
        i = k // n
        j = k % n
        
        x = x_list[k]
        y = y_list[k]
        title = titles[k]
         
        axarr[i, j].plot(x, y)
        axarr[i, j].set_title(title)
    
def save_gallery(x, y, dest, titles=[]):
    gallery(x, y, titles=[])
    plt.savefig(dest)
    plt.clf()
    
def show_gallery(x, y, titles=[]):
    gallery(x, y, titles=[])
    plt.show()  
    plt.clf()  


if __name__ == "__main__":
    x = [1, 2, 3]
    y = [2, 5, 3]
    show(x, y)

    x = [[0, 1, 2], [0, 1, 2]]
    y = [[10, 11, 12], [0, 1, 2]]
    show_gallery(x, y)

    x = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    y = [[10, 11, 12], [0, 1, 2], [0, 1, 2]]
    show_gallery(x, y)

    x = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
    y = [[10, 11, 12], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
    show_gallery(x, y)
