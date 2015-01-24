from mpf.processors import Difference 
from mpf.processors import ImFourierTransform, ReFourierTransform



# Difference
def test_difference():
    difference = Difference()
    
    data = [1, 2, 3, 4, 5]
    
    assert difference.work(data) == [2-1, 3-2, 4-3, 5-4]
    

# Fourier transform


