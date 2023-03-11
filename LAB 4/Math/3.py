import math

n = int(input("Input number of sides: "))
a = float(input("Input the length of a side: "))
area = (n * a ** 2) / (4 * math.tan(math.pi/n))

print(f"The ara of the polygon is: {area:0.0f}")