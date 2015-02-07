from mpf.workers.abstracts import XYWorker
import mpf.processors as processors



class Identity(XYWorker):

    def __init__(self):
        self.processor = processors.Identity()
