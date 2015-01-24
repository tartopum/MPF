from mpf.models.data import DataDict



def test_get():
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
