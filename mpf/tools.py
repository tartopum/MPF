"""A collection of functions."""

import matplotlib.pyplot as plt


__all__ = ('flatten')


def flatten(l, i=0):
    """Flatten the nested list ``l`` by collecting the ith element of its 
    children.
    """
    
    return [line[i] for line in l]

def plot_correlogram(k, ylabel):
    """Plot `k` as a correlogram.
    
    :param k: A list of numbers.
    :type k: list
    """

    x = list(range(len(k)))

    for i in x:
        plt.plot([i, i], [0, k[i]], 'b-')

    plt.plot(x, k, 'bo')
    plt.axhline(0, color='black')
    plt.xlabel('Lag')
    plt.ylabel(ylabel)
