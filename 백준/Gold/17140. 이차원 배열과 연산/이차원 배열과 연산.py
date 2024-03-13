from collections import defaultdict


def check(arr):
    n = len(arr)
    m = len(arr[0])
    if n >= m:
        return 1
    else:
        return 0


def r_cal(arr):
    new_arr = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        dic = defaultdict(int)
        for j in range(len(arr[i])):
            if arr[i][j] == 0: continue
            dic[arr[i][j]] += 1
        tmp = []
        for (k, v) in dic.items():
            tmp.append((k, v))
        tmp.sort(key=lambda x: (x[1], x[0]))
        for (k, v) in tmp:
            new_arr[i].append(k)
            new_arr[i].append(v)
    for i in range(len(new_arr)):
        if len(new_arr[i]) > 100:
            new_arr[i] = new_arr[:100]
    return new_arr


def c_cal(arr):
    new_arr = [[0] * (len(arr[0])) for _ in range(100)]
    for i in range(len(arr[0])):
        dic = defaultdict(int)
        for j in range(len(arr)):
            if arr[j][i] == 0: continue
            dic[arr[j][i]] += 1
        tmp = []
        for (k, v) in dic.items():
            tmp.append((k, v))
        tmp.sort(key=lambda x: (x[1], x[0]))

        for j in range(0, (len(tmp) * 2), 2):
            (k, v) = tmp[j // 2]
            new_arr[j][i] = k
            new_arr[j + 1][i] = v
    for i in range(len(new_arr) - 1, -1, -1):
        if new_arr[i].count(0) == len(new_arr[0]):
            new_arr.pop()
        else:
            break
    return new_arr


def r_fill(arr):
    l = 0
    for k in range(len(arr)):
        l = max(len(arr[k]), l)
    for i in range(len(arr)):
        if len(arr[i]) < l:
            for j in range(l - len(arr[i])):
                arr[i].append(0)


def c_fill(arr):
    l = len(arr)
    for i in range(l):
        if len(arr[i]) < l:
            for j in range(l - len(arr[i])):
                arr[i].append(0)


r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
ans = 0

while 1:
    try:
        if arr[r - 1][c - 1] == k:
            break
    except:
        pass
    if ans >= 100:
        print(-1)
        exit()
    num = check(arr)
    if num:
        arr = r_cal(arr)
        ans += 1
        try:
            if arr[r - 1][c - 1] == k:
                break
        except:
            pass
        r_fill(arr)
    else:
        arr = c_cal(arr)
        ans += 1
        try:
            if arr[r - 1][c - 1] == k:
                break
        except:
            pass
        c_fill(arr)
print(ans)
