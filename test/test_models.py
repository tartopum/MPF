from mpf.models import DataDict



# DataDict
def test_init():
    root = DataDict(key=None, parent=None)
    
    child1 = root.add_child("child1")
    child2 = root.add_child("child2")
    
    child11 = child1.add_child("child11")
    
    child11["element1"] = 1
    
    assert child11.get_parent_keys() == ["child11", "child1", None]
