# -*-coding: utf-8 -*-

from math import sqrt, ceil
from PIL import Image
from globals import get_filenames, get_graph_names, get_numeros

def get_canvas(filenames, max_size):
    canvas = None
    
    filenames.sort()
    filenames_len = len(filenames)
    side_len = int(ceil(sqrt(filenames_len)))
    
    for i in range(filenames_len):
        filename = filenames[i]
        
        im = Image.open(filename)
        im.thumbnail((max_size, max_size), Image.ANTIALIAS)
        width, height = im.size
        
        if canvas is None:
            canvas = Image.new("RGB", (width * side_len, height * side_len), "white")
        
        x = width * (i % side_len)
        y = height * (i // side_len)
        canvas.paste(im, (x, y))
        
    return canvas
    
def main():
    filenames = get_filenames()
    graph_names = get_graph_names()
    max_size = 400
    
    for num in get_numeros():
        for graph_name in graph_names:
            data = [f for f in filenames if num in f and graph_name in f and not "gallery" in f]
            print num + "/gallery/" + graph_name
            canvas = get_canvas(data, max_size)
            canvas.save("../data/" + num + "/gallery/" + graph_name)

if __name__ == "__main__":
    main()
