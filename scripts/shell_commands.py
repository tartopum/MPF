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
                print command
                call(command.split(" "))
            
            # Moving average
            moving_average_reps = ["1"]
            moving_average_steps = ["2", "5", "7"]
            
            for moving_average_rep in moving_average_reps:
                for moving_average_step in moving_average_steps:
                    moving_average = path.joinpath(dirname, 
                                                   "moving-average_" + 
                                                   moving_average_rep + "x_" + 
                                                   moving_average_step + ".png")
                    
                    if not moving_average in filenames:
                        command = ("python moving_average.py " + filename + " " + 
                                   moving_average_rep + " " + moving_average_step)
                        print command
                        call(command.split(" "))
            
            
            
            # Fourier transform
            ft_re = path.joinpath(dirname, "fourier-transform_re.png")
            ft_im = path.joinpath(dirname, "fourier-transform_im.png")
            
            if not (ft_re in filenames and ft_im in filenames):
                command = "python fourier_transform.py " + filename
                print command
                call(command.split(" "))
                
            
            # Least squares
            least_squares = path.joinpath(dirname, "least-squares_thresh50.png")
            if not least_squares in filenames:    
                command = "python least_squares.py " + filename + " 50"
                print command
                call(command.split(" "))
            

if __name__ == "__main__":
    main()
