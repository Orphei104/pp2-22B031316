def filter_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    return [x for x in numbers if is_prime(x)]

print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))