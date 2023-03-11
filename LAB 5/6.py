import re

def replace(string):
    pattern = r"[,.]"
    new_str = re.sub(pattern, ":", string)
    return new_str

a = str(input())
print(replace(a))
