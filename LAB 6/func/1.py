def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = [2, 4, 6, 8, 10]
print(numbers)
print(multiply(numbers))