import copy



class Worker:
    """
        TODO
    """

    def __init__(self):
        self.dest = ""
        self.force = False
        
        self.serializer = None
        self.view = None
    
    @classmethod
    def cache(cls, func):
        def wrapper(obj, datagroup, *args):
            if not obj.force: 
                cache = obj.serializer.load(obj.dest)
                
                if cache is not None:
                    print(obj.dest + " exists.")
                    
                    return cache
            
            # Do not alter args
            datagroup = copy.deepcopy(datagroup)
        
            return func(obj, datagroup, *args)
            
        return wrapper
        
    def work(self):
        raise RuntimeError("'work' method must be implemented.")
        
        
class XYWorker(Worker):
    """
        TODO
    """

    def __init__(self):
        pass
    
    @Worker.cache  
    def work(self, datagroup):
        # Build data
        for dataset in datagroup.datasets:
            x = dataset.contents["x"]
            y = dataset.contents["y"]
            
            x, y = self.processor.work(x, y)
            
            self.view.add({
                "x": x, 
                "y": y, 
                "name": dataset.name
            })
        
        self.view.save(self.dest)
        self.serializer.save(datagroup, self.dest)
        
        return datagroup
