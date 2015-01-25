from mpf.models import Cow
from mpf.models import DataDict
from mpf.models import Serializer



# Cow
def test_cow():
    nums = [1, 21, 123, 1534]
    strings = ["0001", "0021", "0123", "1534"]
    
    for i in range(len(nums)):
        cow = Cow(num=nums[i])    
        
        assert int(cow) == nums[i]
        assert str(cow) == strings[i]
    
    
# DataDict
def test_data():
    def func(a, b):
        return [a, b]
        
    data = DataDict()
    
    a = "a"
    b = "b"
    
    getters = [{
        "key": "key",
        "callable": func,
        "params": (a, b)
    }]
    
    data.get(getters)
    
    assert data["key"] == [a, b]
    
    
# Serializer
def test_serializer():
    exts = [".data", "data"]
    san_exts = [".data", ".data"]
    
    for i in range(len(exts)):
        s = Serializer(ext=exts[i])
        
        assert s.ext == san_exts[i]
