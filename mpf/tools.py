"""A collection of functions."""


__all__ = ('flatten')


def flatten(l, i=0):
    """Flatten the nested list ``l`` by collecting the ith element of its 
    children.
    """
    
    return [line[i] for line in l]
