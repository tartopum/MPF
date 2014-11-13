import numpy as np

class FourierTransform:
    def __init__(self, real=True, timestep=1):
        # Define helpers
        self.fft = np.fft.rfft if real else np.fft.fft
        self.freq = np.fft.fftfreq
        self.shift = np.fft.fftshift
        
        self.real = real
        self.timestep = timestep
    
    def work(self, data):
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
    
    def work(self, A, B):
        # B = AX
        return np.linalg.lstsq(A, B)[0] # X
    

class MovingAverage:
    def __init__(self, step):
        self.step = step
    
    def work(self, x, y):
        # Not to alter args
        x = x + []
        y = y + []
        
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
    
    
