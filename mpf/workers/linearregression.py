from mpf.workers.abstracts import Worker
import mpf.processors as processors



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
        
        return datagroup
