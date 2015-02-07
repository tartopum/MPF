from mpf.workers import Difference
from mpf.workers import Identity
from mpf.workers import LinearRegression
from mpf.workers import MovingAveraging
from mpf.workers import Statistics



def test_difference():
    difference = Difference()
    

def test_identity():
    identity = Identity()
    
    
def test_linear_regression():
    linreg = LinearRegression(percentage=80)
    
    
def test_moving_averaging():
    ma = MovingAveraging(step=2)
    
    
def test_statistics():
    stats = Statistics()
