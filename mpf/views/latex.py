import matplotlib.pyplot as plt

from pylatex import Document, Plt

__all__ = ("LaTeX")



class LaTeX:
    """TODO"""

    def __init__(self, dest, title):
        """TODO"""
        
        self.doc = Document(dest, title=title)
