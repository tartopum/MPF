import numpy as np

class FourierTransform:
    def __init__(self, real=True, timestep=1):
        # Define helpers
        self.fft = np.fft.rfft if real else np.fft.fft
        self.freq = np.fft.fftfreq
        self.shift = np.fft.fftshift
        
        self.real = real
        self.timestep = timestep
    
    def process(self, data):
        # Prepare data
        data = np.asarray(data)
        
        # Run (R)FFT
        spectrum = self.fft(data)
        freq = self.freq(len(spectrum), d=self.timestep)
        freq = self.shift(freq)
        
        return freq, np.real(spectrum), np.imag(spectrum)
    

class LeastSquares:
    def __init__(self):
        pass
    
    def process(self, x, y):
        _x = sum(x)/len(x)
        _y = sum(y)/len(y)
        
        a_num = 0
        a_den = 0
        for i in range(len(x)):
            a_num += (x[i] - _x) * (y[i] - _y)
            a_den += (x[i] - _x)**2
        
        a = a_num/a_den
        b = _y - a * _x
        
        x = np.array(x)
        
        return x, a*x + b
    

class MovingAverage:
    def __init__(self, step, rep=1):
        # 'step' and 'rep' are integers greater than 1
        self.step = max(1, int(step))
        self.rep = max(1, int(rep))
    
    def process(self, x, y):
        # Not to alter args
        x = x + []
        y = y + []
        
        for i in range(self.rep):
            x = x[self.step:len(x) - self.step]     
            
            average_y = []
            for k in range(self.step, len(y)-self.step):
                # Sum 'step' y before and after the current one,
                # which is y[k]
                s = sum(y[k-self.step:k+self.step+1])
                
                average = float(s) / (2*self.step + 1)
                average_y.append(average) 
                
            y = average_y
        
        return x, y
    
    
