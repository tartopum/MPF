from os.path import join



class Factory:

    def __init__(self, root, serializer=None):
        self.root = root
        self.serializer = serializer

    def produce(self, worker, dest, view, serializer=None, force=False):
        worker.dest = join(self.root, dest)
        worker.force = force
        worker.serializer = serializer if serializer is not None else self.serializer
        worker.view = view
        
        return worker
