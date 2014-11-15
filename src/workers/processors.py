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
    
    def data_from_indexes(self, data, indexes):
        l = len(data[0])
        
        return [[line[i] for i in range(l) if i in indexes] for line in data]
        
    def work(self, data):
        l = len(data[0])
        nb = int(l * self.percentage / 100)
        indexes = self.alea_indexes(0, l, nb)
        
        data = self.data_from_indexes(data, indexes)
        
        return data
    
class LinearRegression:
    # http://adventuresinoptimization.blogspot.fr/2011/02/data-fitting-part-2-very-very-simple.html
    
    def __init__(self):
        pass
    
    def compare(self, A, X, B):
        # ||B - AX||
        B = np.array(B)
        A = np.vstack(A)
        X = np.array(X)
        
        return np.linalg.norm(B - A.dot(X)).tolist()
    
    def work(self, A, B):
        # B = AX
        B = np.array(B)
        A = np.vstack(A)
        
        return np.linalg.lstsq(A, B)[0].tolist() # X
    
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
    alea = AleaValues(100)
    
    A = [
        [1, 9, 9**2, 4, 4**2, 9, 9**2],
        [1, 8, 8**2, 6, 6**2, 4, 4**2],
        [1, 9, 9**2, 4, 4**2, 8, 8**2],
        [1, 3, 3**2, 7, 7**2, 9, 9**2],
        [1, 6, 6**2, 8, 8**2, 5, 5**2],
        [1, 4, 4**2, 5, 5**2, 3, 3**2]
    ]
    B = [9, 10, 2, 4, 2, 10]
    
    A_alea, B_alea = alea.work([A, B])
    
    linear_reg = LinearRegression()
    
    X = linear_reg.work(A_alea, B_alea)
    print(X)
    print("")
    
    diff = linear_reg.compare(A, X, B)
    print(diff)
     
