"""Contain a function to difference crude data."""

__all__ = ('difference', 'truncate')


def truncate(data):
    """Truncate the data, as if it had been differenced. These are not
    altered.

    :param data: The data to be truncated.
    :type data: list

    :return: The truncated data.
    :rtype: list
    """

    return data[1:]

def difference(data):
    """Difference the data. These are not altered.

    :param data: The data to be differenced.
    :type data: list

    :return: The differenced data.
    :rtype: list
    """

    return [data[i] - data[i-1] for i in range(1, len(data))]
