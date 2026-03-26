class reverseiter:
    def __init__(self , text):
        self.text = text
        self.index = len(text) - 1  #start from last char

    def __iter__(self):
        return self;

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        
        result = self.text[self.index]
        self.index -= 1
        return result
    

rev = reverseiter("Yushii")

print(next(rev))
print(next(rev))
print(next(rev))