def ident_elements(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return max(count.values())
arr = [1, 2, 3, 2, 2, 3, 4, 4, 4, 4]
print(ident_elements(arr))  