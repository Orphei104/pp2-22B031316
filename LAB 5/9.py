import re

def spaces(string):
    words = re.findall('[A-Z][^A-Z]*', string)
    return " ".join(words)

print(spaces("JavaC#DjangoXcodeSwiftDartC++"))