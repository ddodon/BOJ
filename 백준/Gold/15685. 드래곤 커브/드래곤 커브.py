di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

def curve(loc):
    ci, cj, lst = loc
    tlst = lst[::-1]
    for d in lst:
        ni = ci + di[(d + 1) % 4]
        nj = cj + dj[((d + 1) % 4)]
        arr[ni][nj] = 1
        ci, cj = ni, nj
        tlst.append((d + 1) % 4)
    tlst = tlst[::-1]
    return (ci, cj, tlst)

def cal():
    res = 0
    for i in range(100):
        for j in range(100):
            if all([arr[i][j],arr[i + 1][j],arr[i][j + 1],arr[i + 1][j + 1]]):
                res+=1
    return res


N = int(input())
arr = [[0] * 101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    arr[y][x] = 1
    ni = y + di[d]
    nj = x + dj[d]
    arr[ni][nj] = 1
    loc = (ni, nj, [d])
    for _ in range(g):
        loc = curve(loc)
print(cal())