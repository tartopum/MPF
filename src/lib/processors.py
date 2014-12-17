from random import randint
import numpy as np

#
# ARMA
#
class ARMA:
    def __init__(self):
        pass

#
# Difference
#
class Difference:
    def __init__(self):
        pass
        
    def work(self, x, y):
        diffs = []
        
        for i in range(len(x) - 1):
            diffs.append(y[i+1] - y[i])

        return x[:-1], diffs

#
# Fourier Transform
#
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

class ImFourierTransform(FourierTransform):
    def __init__(self, real=True, timestep=1):
        FourierTransform.__init__(self, real=True, timestep=1)
        
    def work(self, data):
        freq, real, imag = FourierTransform.work(self, data)
        
        return freq, imag

class ReFourierTransform(FourierTransform):
    def __init__(self, real=True, timestep=1):
        FourierTransform.__init__(self, real=True, timestep=1)
        
    def work(self, data):
        freq, real, imag = FourierTransform.work(self, data)
        
        return freq, real

#
# Identity
#
class Identity:
    def __init__(self):
        pass
        
    def work(self, x, y):
        return x, y        

#
# Linear regression
#
class AleaValues:
    def __init__(self, percentage):
        self.percentage = percentage
    
    def alea_indexes(self, begin, end, nb):
        indexes = []
        i = 0
        
        while i < nb:
            k = randint(begin, end-1)
            
            if k in indexes:
                continue
                
            indexes.append(k)
            i += 1
            
        return indexes
        
    def work(self, x, y):
        l = len(x)
        nb = int(l * self.percentage / 100)
        indexes = self.alea_indexes(0, l, nb)
        
        x = [x[i] for i in range(l) if not i in indexes]
        y = [y[i] for i in range(l) if not i in indexes]  
        
        return x, y 
    
class LinearRegression:
    # http://adventuresinoptimization.blogspot.fr/2011/02/data-fitting-part-2-very-very-simple.html
    
    def __init__(self):
        pass
    
    def compare(self, A, X, B):
        return np.linalg.norm(B-A*X)
    
    def work(self, A, B):
        # B = AX
        return np.linalg.lstsq(A, B)[0] # X
    
#
# Moving average
#
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
    

if __name__ == "__main__":
    alea_values = AleaValues(20)
    
    x = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]]
    y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
    
    x, y = alea_values.work(x, y)
    
    linear_reg = LinearRegression()
    A = np.vstack([
        [9, 4, 9],
        [8, 6, 4],
        [9, 4, 8],
        [3, 7, 9],
        [6, 8, 5],
        [4, 5, 3]
    ])
    B = np.array([2,5,8,1,3,4])
    
    X = linear_reg.work(A, B)
    print(X)
     
