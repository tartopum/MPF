class Cow:
    def __init__(self, num):
        self.num = num
        
    def __int__(self):
        return self.num
        
    def __str__(self):
        num = str(self.num)
        
        return "0" * (4 - len(num)) + num
        
        
if __name__ == "__main__":
    
    nums = [1, 11, 123, 5214, 55555]
    
    for num in nums:
        c = Cow(num)
        i = int(c)
        s = str(c)
        
        print(i)
        print(s)
