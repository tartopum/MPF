class Worker:

    def __init__(self, dest="", force=False, serializer=None):
        self.data = None
        self.dest = dest
        self.force = force
        
        self.serializer = serializer
    
    def cache(self):
        if not self.force: 
            cache = self.serializer.load(self.dest)
            
            if cache is not None:
                print(self.dest + " exists.")
                
                return cache
                
        return None
        
    def work(self):
        raise RuntimeError("'work' method must be implemented.")
        
        
class XYWorker(Worker):

    def __init__(self, dest="", force=False, serializer=None):
        Worker.__init__(self, dest, force, serializer)
        
    def work(self, wg):
        cache = self.cache()
        if cache is not None: return cache
        
        # Build data
        for series in wg.series:
            x = series.data["x"]
            y = series.data["y"]
            
            x, y = self.processor.work(x, y)
            
            wg.view.add({
                "x": x, 
                "y": y, 
                "name": series.name
            })
        
        wg.view.save(self.dest)
        self.serializer.save(wg, self.dest)
        
        return wg
