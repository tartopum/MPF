__all__ = ("process")


def process(data):
    """Difference `data`.
    
    :param data: the data to be differenced
    :type data: list
    
    :return: differenced data
    :rtype: list
    """
    
    return [data[i+1] - data[i] for i in range(len(data) - 1)]
