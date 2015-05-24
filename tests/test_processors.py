"""Test the processors."""

from mpf.processors import diff, ma


# Difference
def test_diff_difference():
    data = [1, 2, 3, 4, 5]

    assert diff.difference(data=data) == [2-1, 3-2, 4-3, 5-4]
    
def test_diff_truncate():
    data = [1, 2, 3, 4, 5]

    assert diff.truncate(data=data) == [2, 3, 4, 5]

# MovingAveraging
def test_ma_smooth():
    step = 1
    d = 2*step + 1
    data = [10, 15, 8, 3, 14, 7]
    
    assert ma.smooth(data=data, step=step) == [(10+15+8)/d, (15+8+3)/d, 
                                               (8+3+14)/d, (3+14+7)/d]
                                               
def test_ma_truncate():
    step = 2
    data = [1, 2, 3, 4, 5, 6, 7]
    
    assert ma.truncate(data=data, step=step) == [3, 4, 5]
