def reverse(sentence):
    return ' '.join(sentence.split()[::-1])

a = str(input())
print(reverse(a))