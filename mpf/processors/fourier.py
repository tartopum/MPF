import numpy as np



class FourierTransform:
    """TODO"""

    def __init__(self, real=True, timestep=1):
        """
        TODO
        """
        
        # Define helpers
        self.fft = np.fft.rfft if real else np.fft.fft
        self.freq = np.fft.fftfreq
        self.shift = np.fft.fftshift
        
        self.real = real
        self.timestep = timestep
    
    def process(self, data):
        """
        TODO
        """
        
        # Prepare data
        data = np.asarray(data)
        
        # Run (R)FFT
        spectrum = self.fft(data)
        freq = self.freq(len(spectrum), d=self.timestep)
        freq = self.shift(freq)
        
        return freq, np.real(spectrum), np.imag(spectrum)


class ImFourierTransform(FourierTransform):
    """TODO"""
    

    def __init__(self, real=True, timestep=1):
        """
        TODO
        """
        
        FourierTransform.__init__(self, real=real, timestep=timestep)
        
    def process(self, data):
        """
        TODO
        """
        
        freq, real, imag = self.work(self, data)
        
        return freq, imag


class ReFourierTransform(FourierTransform):
    """TODO"""
    

    def __init__(self, real=True, timestep=1):
        """
        TODO
        """
        
        FourierTransform.__init__(self, real=real, timestep=timestep)
        
    def process(self, data):
        """
        TODO
        """
        
        freq, real, imag = self.work(self, data)
        
        return freq, real
