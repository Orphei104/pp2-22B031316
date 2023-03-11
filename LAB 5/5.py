import re

pattern = r'a.*b$'
test_strings = ['acb', 'aab', 'axb', 'abc', 'adb']
for test_string in test_strings:
    match = re.search(pattern, test_string)
    if match:
        print(f"{test_string} matched the pattern")
    else:
        print(f"{test_string} did not match the pattern")
