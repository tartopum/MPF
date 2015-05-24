"""Functions to process moving averaging."""

__all__ = ('smooth', 'truncate')


def truncate(data, step):
    """Truncate the data ``data`` as if it had been applied a moving average
    with the step ``step``.

    :param data: The data to truncate.
    :param step: The step of the virtual moving average.

    :type data: list
    :type step: int
    """

    return data[step:-step]

def smooth(data, step):
    """Apply a moving average to the data. These are not altered.

    :param data: The data to be smoothed.
    :param step: The step of the moving average.

    :type data: list
    :type step: int

    :return: The smoothed data.
    :rtype: list
    """

    width = 2*step + 1
    smoothed_data = []

    for k in range(len(data) - 2*step):
        average = float(sum(data[k:k+width])) / width
        smoothed_data.append(average)

    return smoothed_data
