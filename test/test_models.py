from mpf.models import DataDict
from mpf.models.cache import Cache



# DataDict
def test_init():
    root = DataDict(key=None, parent=None)
    
    child1 = root.add_child("child1")
    child2 = root.add_child("child2")
    
    child11 = child1.add_child("child11")
    
    child11["element1"] = 1

def test_get_parent_keys():
    root = DataDict(key=None, parent=None)
    
    child1 = root.add_child("child1")
    child2 = root.add_child("child2")
    
    child11 = child1.add_child("child11")
    
    child11["element1"] = 1
        
    assert child11.get_parent_keys() == ["child11", "child1"]
    
    
# Cache
def test_get_filename():
    cache = Cache(directory="./")
    root = DataDict(key=None, parent=None)
    
    child1 = root.add_child("child1")
    child11 = child1.add_child("child11")
    child11["element1"] = 1
    
    child2 = root.add_child(("child2", 4))
    child2[("key", 1)] = 3
    
    assert cache.get_filename(child11, "element1") == "child1-child11-element1"
    assert cache.get_filename(child2, ("key", 1)) == "child2-4-key-1"
    
def test_save_data():
    cache = Cache(directory="./")
    root = DataDict(key=None, parent=None)
    
    child1 = root.add_child("child1")
    child11 = child1.add_child("child11")
    child11["element1"] = 1
    
    child2 = root.add_child(("child2", 4))
    child2[("key", 1)] = 3
    
    cache.save_data(child11, "element1")

def test_get_data():
    cache = Cache(directory="./")
    root = DataDict(key=None, parent=None)
    
    child1 = root.add_child("child1")
    child11 = child1.add_child("child11")
    child11["element1"] = 1
    
    child2 = root.add_child(("child2", 4))
    child2[("key", 1)] = 3
    
    test_save_data()
        
    assert cache.get_data(child11, "element1") == 1
    
    
