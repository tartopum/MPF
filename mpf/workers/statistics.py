from mpf.workers.abstracts import Worker
import mpf.processors as processors



class Statistics(Worker):

    def __init__(self):
        self.processor = processors.Statistics()
    
    @Worker.cache
    def work(self, datagroup):
        # Build data
        data = [dataset.contents[self.key] for dataset in datagroup.datasets]
        measures = self.processor.work(data)
        datagroup.metadata.update(measures)
        
        measures["name"] = str(datagroup.name)
        self.view.add(measures)
        
        self.view.save(self.dest)    
        self.serializer.save(datagroup, self.dest)
        
        return datagroup
