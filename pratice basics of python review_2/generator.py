def even_numbers(max_limit):
    current = 0
    while current <= max_limit:
        yield current
        current += 2


#usage
for num in even_numbers(10):
    print(num)