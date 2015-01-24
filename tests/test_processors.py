from mpf.processors import AleaValues
from mpf.processors import Difference 
from mpf.processors import ImFourierTransform, ReFourierTransform
from mpf.processors import MovingAveraging



# Difference
def test_difference():
    difference = Difference()
    
    data = [1, 2, 3, 4, 5]
    
    assert difference.work(data=data) == [2-1, 3-2, 4-3, 5-4]
    

# Fourier transform


# Alea values
def test_alea_values():
    a = AleaValues(percentage=80)
    
    data = [[1, 2, 3]]
    
    a.work(data=data)
    
    
# MovingAveraging
def test_ma():
    step = 1
    d = 2*step + 1
    
    ma = MovingAveraging(step=step)
    
    x = [1, 2, 3, 4, 5, 6]
    y = [10, 15, 8, 3, 14, 7]
    
    assert ma.work(x=x, y=y) == ([2, 3, 4, 5], [(10+15+8)/d, (15+8+3)/d, 
                                               (8+3+14)/d, (3+14+7)/d])
