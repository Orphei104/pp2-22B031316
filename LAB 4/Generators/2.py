def even_num(n):
    for i in range(0, n+1, 2):
        yield str(i)

a = 21
even = even_num(a)
even_string = ",".join(even)
print(f"0 and {a} |", even_string)