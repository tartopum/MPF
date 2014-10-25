# -*-coding: utf-8 -*-

import os.path
import sys
import numpy as np
import matplotlib.pyplot as plt
from globals import draw, ensure_dir, get_filename, get_values

def main(args):
    path = args[0]
    with open(path, "r") as f:
        days, amounts = get_values(f)
    
    days = np.asarray(days)
    amounts = np.asarray(amounts)
    
    spectrum = np.fft.fft(amounts)
    timestep = 1
    freq = np.fft.fftfreq(len(spectrum), d=timestep)
    freq = np.fft.fftshift(freq)
    spectrum = np.fft.fftshift(spectrum)
    
    filename = get_filename(path, "fourier-transform_re")
    title = filename
    plt.plot(freq, np.real(spectrum))
    draw(filename, title=title, xlabel="Frequencies (Hz)", ylabel="Spectrum (Re)")
    
    filename = get_filename(path, "fourier-transform_im")
    title = filename
    plt.plot(freq, np.imag(spectrum))
    draw(filename, title=title, xlabel="Frequencies (Hz)", ylabel="Spectrum (Im)")
    
    
if __name__ == "__main__":
    main(sys.argv[1:])
