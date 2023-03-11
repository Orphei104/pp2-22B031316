import re

pattern = r'[A-Z][a-z]+'
test_string = "The Quick Brown Fox Jumps Over The Lazy Dog"
matches = re.findall(pattern, test_string)

for match in matches:
    print(match)
