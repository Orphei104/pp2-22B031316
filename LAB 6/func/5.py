def alltrue(t):
    return all(t)

true1 = (True, True, True)
true2 = (False, True, False)

print(f"all elements of tuple {true1} are {alltrue(true1)}")
print(f"all elements of tuple {true2} are {alltrue(true2)}")