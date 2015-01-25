from mpf.tools import add_ext



# add_ext
def test_add_ext():
    exts = [".ext", ".ext"]
    paths = ["path", "path.ext"]
    extpaths = ["path.ext", "path.ext"]
    
    for i in range(len(exts)):
        ext = exts[i]
        path = paths[i]
        extpath = extpaths[i]
        
        assert add_ext(path=path, ext=ext) == extpath
