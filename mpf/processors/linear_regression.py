import numpy as np
from scipy.optimize import leastsq



class LinearRegression:
    """TODO"""
    
    def __init__(self):
        pass
    
    def _compare(self, X, A, B):
        """
        TODO
        """
        
        B = np.array(B)
        A = np.vstack(A)
        X = np.array(X)
        
        return B - A.dot(X)
    
    def error(self, X, A, B):
        """
        TODO
        """
        
        try:
            return np.linalg.norm(self._compare(X, A, B)) # ||A||
        except ValueError:
            return -1
    
    def work(self, A, B):
        """
        TODO
        """
        
        # B = AX
        B = np.array(B)
        A = np.vstack(A)
        
        X0 = np.zeros(A.shape[1])
        args = (A, B)
        
        try:
            return leastsq(self._compare, X0, args)[0] # X
        except TypeError:
            return []