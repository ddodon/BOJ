from collections import defaultdict


def r_opr(arr):
    nrr = []
    mx_row = len(arr)
    mx_col = 0
    for n, lst in enumerate(arr):
        dic = defaultdict(int)
        for num in lst:
            if num == 0: continue
            dic[num] += 1
        tmp = sorted(list(dic.items()), key=lambda x: (x[1], x[0]))
        nlst = []
        for k, v in tmp:
            nlst.append(k)
            nlst.append(v)
        mx_col = max(mx_col, len(nlst))
        nrr.append(nlst)
    arr = [[0] * mx_col for _ in range(mx_row)]
    for i in range(mx_row):
        arr[i][:len(nrr[i])] = nrr[i][:100]
    return arr


def c_opr(arr):
    arr = [list(lst) for lst in zip(*arr)]
    nrr = []
    mx_row = len(arr)
    mx_col = 0
    for n, lst in enumerate(arr):
        dic = defaultdict(int)
        for num in lst:
            if num == 0: continue
            dic[num] += 1
        tmp = sorted(list(dic.items()), key=lambda x: (x[1], x[0]))
        nlst = []
        for k, v in tmp:
            nlst.append(k)
            nlst.append(v)
        mx_col = max(mx_col, len(nlst))
        nrr.append(nlst)
    arr = [[0] * mx_col for _ in range(mx_row)]
    for i in range(mx_row):
        arr[i][:len(nrr[i])] = nrr[i][:100]
    arr = [list(lst) for lst in zip(*arr)]
    return arr


r, c, k = map(int, input().split())
r, c = r - 1, c - 1
arr = [list(map(int, input().split())) for _ in range(3)]
for t in range(101):
    # 1. 정답조건
    try:
        if arr[r][c] == k:
            print(t)
            break
    except:
        pass
    # 2. 행 열 길이 비교
    if len(arr) >= len(arr[0]):
        arr = r_opr(arr)
    else:
        arr = c_opr(arr)
else:
    print(-1)