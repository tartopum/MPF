from mpf.analysis.abstracts import Analysis
from mpf import processors
from mpf import config

__all__ = ("Error", "ParamVector")


class LinRegAnalysis(Analysis):
    
    LBL = "linreg"
    
    @staticmethod
    def format_design_matrix(data):
        """
        B = AX
        
        data = [
            [day1, day2, day3],
            [cons1, cons2, cons3]
        ]
        
        A = [
            [1, day1, day1**2, cons1, cons1**2],
            [1, day2, day2**2, cons2, cons2**2],
            [1, day3, day3**2, cons3, cons3**2]
        ]
        """
        
        A = []
        
        for i in range(len(data[0])):
            line = [1] # Offset
            
            for series in data:
                line.append(series[i])
                line.append(series[i]**2)
            
            A.append(line)
            
        return A
    
    @classmethod
    def get_key(cls, *args, **kwargs):
        return (cls.LBL, kwargs["key"], cls.SUB_LBL, kwargs["proportion"])
        

class Error(LinRegAnalysis):
    
    SUB_LBL = "error"
    
    @classmethod
    def process(cls, lact, *args, **kwargs):
        A, B = cls.format_design_matrix(kwargs["A"]), kwargs["B"]
        key = ParamVector.get_key(**kwargs)
        
        return processors.linreg.error(lact[key], A, B)


class ParamVector(LinRegAnalysis):
    
    SUB_LBL = "X"
    
    @classmethod
    def process(cls, lact, *args, **kwargs):
        A, B = cls.format_design_matrix(kwargs["A"]), kwargs["B"]
        A_alea, B_alea = processors.alea.process([A, B], kwargs["proportion"])
        
        return processors.linreg.process(A_alea, B_alea)
