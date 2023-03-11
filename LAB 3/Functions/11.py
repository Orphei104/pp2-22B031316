def is_palindrome(sentence):
    return sentence == sentence[::-1]

a = str(input())
print(is_palindrome(a))