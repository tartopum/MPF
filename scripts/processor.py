import numpy as np

class Processor():
    def __init__(self):
        pass   
    
    # Fourier transform
    #
    def fourier_transform(self, data, real=True, timestep=1):
        # Define helpers
        fft = np.fft.rfft if real else np.fft.fft
        freq = np.fft.fftfreq
        shift = np.fft.fftshift
        
        # Prepare data
        data = np.asarray(data)
        
        # Run (R)FFT
        spectrum = fft(data)
        freq = freq(len(spectrum), d=timestep)
        freq = shift(freq)
        
        return freq, np.real(spectrum), np.imag(spectrum)
        
    # Least squares
    #
    def least_squares(self, x, y):
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
        
    # Moving average
    #
    def moving_average(self, x, y, step, rep=1):
        # 'step' and 'rep' are integers greater than 1
        step = max(1, int(step))
        rep = max(1, int(rep))
        
        # Not to alter args
        x = x + []
        y = y + []
        
        for i in range(rep):
            x = x[step:len(x) - step]     
            
            average_y = []
            for k in range(step, len(y)-step):
                # Sum 'step' y before and after the current one,
                # which is y[k]
                s = sum(y[k-step:k+step+1])
                
                average = float(s) / (2*step + 1)
                average_y.append(average) 
                
            y = average_y
        
        return x, y
        
        
if __name__ == "__main__":
    obj = Processor()
