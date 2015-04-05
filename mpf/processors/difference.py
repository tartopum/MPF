__all__ = ("process")


def process(data):
    """Process the difference between an element in the `data` list and the 
    next one.
    
    :param data: the data to be processed
    :type data: list
    
    :return: the list of differences
    :rtype: list
    """
    
    return [data[i+1] - data[i] for i in range(len(data) - 1)]
