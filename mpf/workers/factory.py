from os.path import join



class Factory:
    """A class configurating workers."""

    def __init__(self, data_path=""):
        """
        :param data_path: The path where to save data.
        
        :type data_path: str
        """
        
        self.data_path = data_path

    def configurate(self, worker, view, getter, serializer, force=False):
        """Configurate the worker. Alter it.
        
        :param worker: The worker to configurate.
        :param view: The view to use to display data.
        :param getter: A function to get needed data among the ones given to 
        the worker.
        :param serializer: The serializer used to cache data.
        :param force: Whether cache must be used or not.
        
        :type worker: object
        :type view: object
        :type getter: func
        :type serializer: object
        :type force: bool
        """
        
        # View
        view.dest = join(data_path, view.dest)
        worker.view = view
        
        # Getter
        worker.getter = getter
        
        # Serializer
        serializer.dest = join(data_path, serializer.dest)
        worker.serializer = serializer
        
        # Force
        worker.force = force
        
        
