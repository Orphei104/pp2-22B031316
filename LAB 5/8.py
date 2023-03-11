import re

def splitup(string):
    words = re.findall('[A-Z][^A-Z]*', string)
    return words

print(splitup("JavaC#DjangoXcodeSwiftDartC++"))