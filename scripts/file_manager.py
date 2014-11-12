import os.path
import re

class FileManager():
    def __init__(self, src, dest):
        self.set_src(src)
        self.set_dest(dest)
        
    def ensure_dir(self, path):
        d = os.path.dirname(path)
        if not(os.path.exists(d)):
            os.makedirs(d)
    
    def get_cow_data(self, cow):
        if cow in self.get_cows():
            root = os.path.join(self.src, cow)
            data = []

            for f in os.listdir(root):
                f = os.path.join(cow, f)

                if self.is_data(f):
                    lactation = self.get_lactation(f)
                    data.append((lactation, self.read_data(f)))
            
            return data
        else:
            return []

    def get_cows(self):
        return os.listdir(self.src)
    
    def get_lactation(self, path):
        fname, ext = os.path.splitext(path)
        return os.path.basename(fname)

    def is_data(self, f):
        return ".csv" in f

    def read_data(self, path):
        x = []
        y = []
        
        path = os.path.join(self.src, path)
        
        with open(path, "r") as f:
            for line in f.readlines():
                x_val, y_val = line.strip().split(" ")
                
                if x_val == "" or y_val == "":
                    print("Error in " + path + ":")
                    print(line)
                    return [], []
                
                x_val = int(x_val)
                x_val = max(0, x_val) # x_val >= 0
                
                y_val = y_val.replace(",", ".")
                y_val = float(y_val)
                y_val = round(y_val, 2)
                y_val = max(0.0, y_val) # y_val >= 0.0
                    
                x.append(x_val)
                y.append(y_val)
        
        # (i != j) => (x[i] != x[j])
        if len(x) != len(set(x)):
            print("Error in " + path + ": two x are equal.")
            return [], []
                
        return x, y
    
    def sanitize(self, path):
        def sanitize_line(line):
            line = line.strip()
            line = line.replace("\t", " ")
            return line
        
        with open(path, "r") as f:
            lines = f.readlines()
            
        with open(path, "w") as f:    
            lines = lines[2:]
            lines = map(sanitize_line, lines)
            lines = [line for line in lines if line != ""]
            
            txt = "\n".join(lines)
            
            f.write(txt)
        
    def split_filename(filename):
        search = re.search(".+/data/([0-9]+)/([0-9]+)/(.+)$", filename)
        return search.group(1), search.group(2), search.group(3)  
        
    # Setters
    def set_dest(self, path):
        d = os.path.dirname(path)
        assert os.path.exists(d)
        self.dest = path    

    def set_src(self, path):
        d = os.path.dirname(path)
        assert os.path.exists(d)
        self.src = path    


if __name__ == "__main__":        
    obj = FileManager("../data/", "../processing/")
    
    days, amounts = obj.read_data("2251/1/data.txt")
    # print(days)
    # print(amounts)
    print(obj.get_cow_data("2251"))
    
            
