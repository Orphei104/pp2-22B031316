def camel(string):
    words = string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])

print(camel("python_programming"))
print(camel("Java_script"))