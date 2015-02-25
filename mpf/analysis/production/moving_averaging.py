from mpf import processors

__all__ = ("MovingAveraging")



class MovingAveraging:

    steps = [2]
        
    def work(self, cow):
        for step in MovingAveraging.steps:
            ma = processors.MovingAveraging(step)
            
            for lact in cow.get_lacts():
                days_ma, prods_ma = ma.work(lact.days, lact.prods)
                
                lact.add_key(("ma", "days", step), days_ma)
                lact.add_key(("ma", "prods", step), prods_ma)
