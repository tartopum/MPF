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
    

def gallery(x_list, y_list, title="", titles=[], xlabels=[], ylabels=[]):
    l = len(x_list)
    
    if titles == []: titles = ["" for i in range(l)]
    
    if xlabels == []: xlabels = ["" for i in range(l)]
    elif isinstance(xlabels, str): xlabels = [xlabels for i in range(l)]
    
    if ylabels == []: ylabels = ["" for i in range(l)]
    elif isinstance(ylabels, str): ylabels = [ylabels for i in range(l)]
    
    n = int(ceil(sqrt(l)))
    
    fig = plt.figure(num=1, figsize=(10, 8))
    fig.suptitle(title)
    
    for k in range(l):
        x = x_list[k]
        y = y_list[k]
        title = titles[k]
        xlabel = xlabels[k]
        ylabel = ylabels[k]
         
        plt.subplot(1 if l == 2 else n, n, k+1)
        draw(x, y, title, xlabel, ylabel)
    
    plt.tight_layout() # To space subplots
    plt.subplots_adjust(top=0.9) # Not to overwrite title
    
def save_gallery(x, y, dest, title, titles=[], xlabels=[], ylabels=[]):
    gallery(x, y, title, titles, xlabels, ylabels)
    plt.savefig(dest)
    plt.clf()
    
def show_gallery(x, y, title, titles=[], xlabels=[], ylabels=[]):
    gallery(x, y, title, titles, xlabels, ylabels)
    plt.show()  
    plt.clf()  


if __name__ == "__main__":
    x = [1, 2, 3]
    y = [2, 5, 3]
    show(x, y)
    
    x = [[0, 1, 2], [0, 1, 2]]
    y = [[10, 11, 12], [0, 1, 2]]
    titles = ["1", "2"]
    show_gallery(x, y, "TITLEEEEE", titles, "xx")
    
    x = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    y = [[10, 11, 12], [0, 1, 2], [0, 1, 2]]
    titles = ["1", "2", "3"]
    show_gallery(x, y, "TITLEEEEE", titles)

    x = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
    y = [[10, 11, 12], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
    titles = ["1", "2", "3", "4"]
    show_gallery(x, y, "TITLEEEEE", titles)
    
    
