from mpf.workers.abstracts import XYWorker
import mpf.processors as processors



class Difference(XYWorker):

    def __init__(self):
        self.processor = processors.Difference()
