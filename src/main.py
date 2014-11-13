import os.path

from file_manager import FileManager
from drawer import Drawer
from processor import Processor

drawer = Drawer()
file_manager = FileManager("../data/", "../processing/")
processor = Processor()



def least_squares(filenames):
    path = os.path.join(file_manager.dest, "least-squares")
    file_manager.ensure_dir(path)

    for cow, filenames in :
        

def main():
    for cow in file_manager.get_cows():
        data = file_manager.get_cow_data(cow)

if __name__ == "__main__":
    main(sys.argv[1:])
