def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for number in squares(3, 10):
    print(number)