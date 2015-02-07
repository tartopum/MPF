from mpf.workers.abstracts import XYWorker
import mpf.processors as processors



class MovingAveraging(XYWorker):

    def __init__(self, step):
        self.step = max(1, int(step)) # 'step' is an integer greater than 1
        
        self.processor = processors.MovingAveraging(self.step)   
