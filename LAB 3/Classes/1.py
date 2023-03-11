def myfunc():
    result = []
    for i in range(1, 1001):
        divisors = 0
        for j in range ( 1, int (i ** 0.5) + 1 ):
            if i % j == 0:
                if i / j == j:
                    divisors += 1
                else:
                    divisors += 2
        if divisors == 5:
            result.append (i)
    return result
print(myfunc())