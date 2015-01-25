def add_ext(path, ext):
    """
    TODO
    """
    
    try:
        assert path[len(path)-len(ext):] == ext
    except AssertionError:
        path += ext
    
    return path
