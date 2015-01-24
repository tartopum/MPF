from mpf.processors import AleaValues
from mpf.processors import Difference 
from mpf.processors import ImFourierTransform, ReFourierTransform



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
