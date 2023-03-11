import re

def snake(string):
    words = re.findall('[A-Z][^A-Z]*', string)
    return "_".join(word.lower() for word in words)

print(snake("camelCaseString"))
print(snake("ExampleAmbient"))

