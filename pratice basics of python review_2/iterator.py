class evennumbers:
    def __init__(self , max_limit):
        self.max_limit = max_limit
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.max_limit:
            raise StopIteration
        
        result = self.current
        self.current += 2
        return result
    

even = evennumbers(10)

for num in even:
    print(num)