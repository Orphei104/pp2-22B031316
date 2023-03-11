def celcius(f):
    return int((5 / 9) * (f - 32))

fahrenheit = int(input())
print(celcius(fahrenheit),'°C')