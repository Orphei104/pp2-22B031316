from itertools import permutations

def perm(string):
    return [''.join(p) for p in permutations(string)]

a = input()
print(set(perm(a)))