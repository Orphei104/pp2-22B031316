import time
import math

def milli(n, ms):
    time.sleep(ms / 1000)
    return math.sqrt(n)

n = 25100
ms = 2123
print(f"Square root of {n} after {ms} milliseconds is {milli(n, ms)}")