# -*-coding: utf-8 -*-
from path import path
from subprocess import call

from globals import get_filenames

def main():
    filenames = get_filenames()
    for filename in filenames:
        if "data.txt" in filename:
            dirname = path.dirname(filename)
            
            # Crude values
            crude_values = path.joinpath(dirname, "crude-values.png")
            
            if not crude_values in filenames:    
                command = "python crude_values.py " + filename
                call(command.split(" "))
                print command
            
            # Moving average
            moving_average_rep = "1"
            moving_average_step = "7"
            moving_average = path.joinpath(dirname, 
                                           "moving-average_" + 
                                           moving_average_rep + "x_" + 
                                           moving_average_step + ".png")
            
            if not moving_average in filenames:
                command = ("python moving_average.py " + filename + " " + 
                           moving_average_rep + " " + moving_average_step)
                call(command.split(" "))
                print command
            
            # Fourier transform
            ft_re = path.joinpath(dirname, "fourier-transform_re_rfft.png")
            ft_im = path.joinpath(dirname, "fourier-transform_im_rfft.png")
            
            if not (ft_re in filenames and ft_im in filenames):
                command = "python fourier_transform.py " + filename
                call(command.split(" "))
                print command
            

if __name__ == "__main__":
    main()
