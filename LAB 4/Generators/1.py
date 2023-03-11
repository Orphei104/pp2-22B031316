def square_generator(N):
    for i in range(1, N+1):
        yield i ** 2

square = int(input())
squares = square_generator(square)
for square in squares:
    print(square)
