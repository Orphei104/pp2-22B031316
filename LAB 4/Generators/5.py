def countdown(n):
    while n >= 0:
        yield n
        n -= 1

numbers = countdown(10)

for number in numbers:
    print(number)
