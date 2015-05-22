from mpf.analysis.abstracts import Analysis
from mpf import processors
from mpf import config

__all__ = ("Difference")


class Difference(Analysis):
    
    LBL = "diff"
    
    @classmethod
    def get_key(cls, *args, **kwargs):
        return (cls.LBL, kwargs["label"])

    @classmethod
    def process(cls, cow, *args, **kwargs):
        data = cow.concatenate_lacts(kwargs["key"])

        return processors.diff.process(data)
