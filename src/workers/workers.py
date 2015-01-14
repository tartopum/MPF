from workers.abstracts import Worker, XYWorker
import workers.processors as processors



class Difference(XYWorker):

    def __init__(self):
        self.processor = processors.Difference()


class Identity(XYWorker):

    def __init__(self):
        self.processor = processors.Identity()


class LinearRegression(Worker):

    def __init__(self, percentage):
        self.alea = processors.AleaValues(percentage)
        self.processor = processors.LinearRegression()
    
    def build_A(self, data):
        A = []
        l = len(data[0])
        
        for i in range(l):
            line = [1] # Offset
            
            for series in data:
                line.append(series[i])
                line.append(series[i]**2)
            
            A.append(line)
            
        return A
    
    @Worker.cache    
    def work(self, datagroup):
        # Build data
        for dataset in datagroup.datasets:
            B = dataset.contents["B"]
            A = self.build_A(dataset.contents["A-data"])
            
            A_alea, B_alea = self.alea.work([A, B])
            
            dataset.contents["A"] = A
            dataset.contents["B-alea"] = B_alea
            dataset.contents["A-alea"] = A_alea
            
            X = self.processor.work(A_alea, B_alea)
            dataset.contents["X"] = X
            
            error = self.processor.error(X, A, B)
            dataset.contents["error"] = error
            
            self.view.add({
                "A": A,
                "B": B,
                "A-alea": A_alea,
                "B-alea": B_alea,
                "X": X.tolist(),
                "error": error,
                "name": dataset.name
            })
        
        self.view.save(self.dest)    
        self.serializer.save(datagroup, self.dest)
        
        return datagroup


class MovingAveraging(XYWorker):

    def __init__(self, step):
        self.step = max(1, int(step)) # 'step' is an integer greater than 1
        
        self.processor = processors.MovingAverage(self.step)       
    
    
class Statistics(Worker):

    def __init__(self, key):
        self.key = key
        
        self.processor = processors.Statistics()
        
    def work(self, wg):
        cache = self.cache()
        if cache is not None: return cache
        
        data = [series.data[self.key] for series in wg.series]
        measures = self.processor.work(data)
        
        series.data.update(measures)
        
        wg.view.add(measures)
        
        wg.view.save(self.dest)    
        self.serializer.save(wg, self.dest)
        
        return wg
                
