"""Test the processors."""

from mpf.processors import ma


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
