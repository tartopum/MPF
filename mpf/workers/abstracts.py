import copy



class Worker:
    """An abstract worker."""

    def __init__(self):
        self.force = False
        self.serializer = None
        self.view = None
        self.getter = None
    
    @classmethod
    def work(cls, worker):
        def wrapper(obj, datagroup, *args):
            if not obj.force: 
                cache = obj.serializer.load()
                
                if cache is not None:
                    return cache
            
            # Do not alter args
            datagroup = copy.deepcopy(datagroup)
            datagroup = worker(obj, datagroup, *args)
            
            # Save
            obj.view.save()    
            obj.serializer.save(datagroup)
            
            return datagroup
            
        return wrapper
        
        
class XYWorker(Worker):
    """A worker working with data as x and y."""

    def __init__(self):
        pass
    
    @Worker.work  
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
        
        return datagroup
