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
        
    def work(self, wg):
        cache = self.cache()
        if cache is not None: return cache
        
        # Build data
        for series in wg.series:
            cons = series.data["cons"]
            lact_days = series.data["lact_days"]
            lact = [series.id for i in range(len(cons))]
            
            B = series.data["prods"]
            A = self.build_A([cons, lact_days, lact])
            
            A_alea, B_alea = self.alea.work([A, B])
            
            series.data["A"] = A
            series.data["B_alea"] = B_alea
            series.data["A_alea"] = A_alea
            
            X = self.processor.work(A_alea, B_alea)
            series.data["X"] = X
            
            diff = self.processor.compare(A, X, B)
            series.data["diff"] = diff
            
            wg.view.add({
                "A": A,
                "B": B,
                "A_alea": A_alea,
                "B_alea": B_alea,
                "X": X,
                "diff": diff,
                "name": series.name
            })
        
        wg.view.save(self.dest)    
        self.serializer.save(wg, self.dest)
        
        return wg


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
                
