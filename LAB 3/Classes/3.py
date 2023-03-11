def max_cons_evennum(N, list):
    max_cnt = 0
    cnt = 0
    for i in range(N):
        if list[i] % 2 == 0:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    return max(max_cnt, cnt)
list = [1, 2, 3, 4, 5, 6, 8, 10, 11, 12]
N = len(list)
print(max_cons_evennum(N, list)) 
