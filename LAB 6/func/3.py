def is_pal(string):
    return string == string[::-1]

if is_pal("madam"):
    print("palindrome")
else:
    print("is not palindrome")