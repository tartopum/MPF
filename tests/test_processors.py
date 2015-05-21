from mpf.processors import alea, diff, linreg, ma, stats 


# Difference
def test_difference():
    data = [1, 2, 3, 4, 5]
    assert diff.process(data=data) == [2-1, 3-2, 4-3, 5-4]
    

# Alea values
def test_alea_values():
    data = [[1, 2, 3], [4, 5, 6]]
    
    alea.process(data=data, percentage=80)
    
    
# MovingAveraging
def test_smooth():
    step = 1
    d = 2*step + 1
    data = [10, 15, 8, 3, 14, 7]
    
    assert ma.smooth(data=data, step=step) == [(10+15+8)/d, (15+8+3)/d, 
                                               (8+3+14)/d, (3+14+7)/d]
                                               
def test_truncate():
    step = 2
    data = [1, 2, 3, 4, 5, 6, 7]
    
    assert ma.truncate(data=data, step=step) == [3, 4, 5]
                                               
                                               
# LinearRegression
def test_linreg():
    A = [
        [1, 9, 9**2, 4, 4**2],
        [1, 8, 8**2, 6, 6**2],
        [1, 9, 9**2, 4, 4**2],
        [1, 3, 3**2, 7, 7**2],
        [1, 6, 6**2, 8, 8**2],
        [1, 4, 4**2, 5, 5**2]
    ]
    
    B = [9, 10, 2, 4, 2, 10]
    
    X = linreg.process(A=A, B=B)
    error = linreg.error(X=X, A=A, B=B)
    
    
# Statistics
def test_stats():
    data = [1, 2, 3, 4, 4]
    
    assert stats.process(data=data) == {
                                        "mean": 2.8,
                                        "median": 3,
                                        "mode": 4,
                                        "variance": 1.7
                                    }
    
