from mpf import processors

__all__ = ("MovingAveraging")



class MovingAveraging:

    steps = [2]
    
    label = "ma"
    days_label = "days"
    prods_label = "prods"
    
    @staticmethod
    def get_key(t, step):
        return (
            MovingAveraging.label, 
            t, 
            step
        )
        
    def work(self, cow):
        for step in MovingAveraging.steps:
            ma = processors.MovingAveraging(step)
            
            for lact_key in cow.get_lact_keys():
                lact = cow[lact_key]
                
                days_ma, prods_ma = ma.work(lact["days"], lact["prods"])
                
                days_key = MovingAveraging.get_key(MovingAveraging.days_label, step)
                prods_key = MovingAveraging.get_key(MovingAveraging.prods_label, step)
                
                lact[days_key] = days_ma
                lact[prods_key] = prods_ma
