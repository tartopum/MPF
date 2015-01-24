from mpf.processors import AleaValues
from mpf.processors import Difference 
from mpf.processors import ImFourierTransform, ReFourierTransform
from mpf.processors import LinearRegression
from mpf.processors import MovingAveraging
from mpf.processors import Statistics



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
                                               
                                               
# LinearRegression
def test_linreg():
    linreg = LinearRegression()
    
    A = [
        [1, 9, 9**2, 4, 4**2],
        [1, 8, 8**2, 6, 6**2],
        [1, 9, 9**2, 4, 4**2],
        [1, 3, 3**2, 7, 7**2],
        [1, 6, 6**2, 8, 8**2],
        [1, 4, 4**2, 5, 5**2]
    ]
    
    B = [9, 10, 2, 4, 2, 10]
    
    X = linreg.work(A=A, B=B)
    error = linreg.error(X=X, A=A, B=B)
    
    
# Statistics
def test_stats():
    functions = {
        "mean": Statistics.mean,
        "median": Statistics.median,
        "mode": Statistics.mode,
        "variance": Statistics.variance
    }
    
    stats = Statistics(functions=functions)
    
    data = [1, 2, 3, 4, 4]
    
    assert stats.work(data=data) == {
                                        "mean": 2.8,
                                        "median": 3,
                                        "mode": 4,
                                        "variance": 1.7
                                    }
    
