def square_gen(n):
     for i in range(1 , n+1):
          yield i**2



for num in square_gen(5):
     print(num)


