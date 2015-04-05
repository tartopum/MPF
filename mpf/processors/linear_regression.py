import numpy as np
from scipy.optimize import leastsq

__all__ = ("error", "process")


def _compare(X, A, B):
    """TODO"""
    
    B = np.array(B)
    A = np.vstack(A)
    X = np.array(X)
    
    return B - A.dot(X)

def error(X, A, B):
    """TODO"""
    
    try:
        return np.linalg.norm(_compare(X, A, B)) # ||A||
    except ValueError:
        return -1

def process(A, B):
    """TODO"""
    
    # B = AX
    B = np.array(B)
    A = np.vstack(A)
    
    X0 = np.zeros(A.shape[1])
    args = (A, B)
    
    try:
        return list(leastsq(_compare, X0, args)[0]) # X
    except TypeError:
        return []
