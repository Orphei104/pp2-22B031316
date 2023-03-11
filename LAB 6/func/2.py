def uplow(string):
    upper = 0
    lower = 0
    for count in string:
        if count.isupper():
            upper += 1
        elif count.islower():
            lower += 1
    return upper, lower

str = "TEST EXAMPLE test example"
upper, lower = uplow(str)
print(upper)
print(lower)

