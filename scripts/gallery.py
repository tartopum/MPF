# -*-coding: utf-8 -*-

from PIL import Image

def get_canvas(basepath, max_size):
    canvas = Image.new("RGB", (max_size * 3, max_size * 3))
    
    for i in range(1, 10):
        filename = "moving-average_1x_7.png"
        path = basepath + str(i) + "/" + filename
        
        im = Image.open(path)
        im.thumbnail((max_size, max_size), Image.ANTIALIAS)
        width, height = im.size
        
        x = width * ((i-1) % 3)
        y = height * ((i-1) // 3)
        canvas.paste(im, (x, y))
        
    return canvas
    
def main():
    basepath = "../data/2251/"
    max_size = 400
    
    canvas = get_canvas(basepath, max_size)
    canvas.show()

if __name__ == "__main__":
    main()
