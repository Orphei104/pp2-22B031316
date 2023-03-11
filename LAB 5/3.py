import re

pattern = r'[a-z]+_[a-z]+'

test_string = "this_is_a_test_string"

matches = re.findall(pattern, test_string)

for match in matches:
    print(match)
