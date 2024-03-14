di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def direction(arr, ri, rj, bi, bj, dir):
    flag = False
    blue_in = False
    d = dir
    while 1:
        ni = ri + di[d]
        nj = rj + dj[d]
        if arr[ni][nj] == 'O':
            flag = True
            arr[ri][rj] = '.'
            break
        elif arr[ni][nj] == '.':
            arr[ni][nj] = 'R'
            arr[ri][rj] = '.'
            ri, rj = ni, nj
        else:
            break
    while 1:
        ni = bi + di[d]
        nj = bj + dj[d]
        if arr[ni][nj] == 'O':
            blue_in = True
            flag = False
            arr[bi][bj] = '.'
            break
        elif arr[ni][nj] == '.':
            arr[ni][nj] = 'B'
            arr[bi][bj] = '.'
            bi, bj = ni, nj
        else:
            break
    if not blue_in:
        while 1:
            ni = ri + di[d]
            nj = rj + dj[d]
            if arr[ni][nj] == 'O':
                flag = True
                arr[ri][rj] = '.'
                break
            elif arr[ni][nj] == '.':
                arr[ni][nj] = 'R'
                arr[ri][rj] = '.'
                ri, rj = ni, nj
            else:
                break
    return (blue_in,flag, arr, ri, rj, bi, bj)


def dfs(n, tlst):
    global ans
    if n == 10:
        ri, rj = red
        bi, bj = blue
        arr = [lst[:] for lst in arr_o]
        arr[ri][rj] = 'R'
        arr[bi][bj] = 'B'
        for i in range(10):
            (blue_in, flag, nrr, nri, nrj, nbi, nbj) = direction(arr, ri, rj, bi, bj, tlst[i])
            arr, ri, rj, bi, bj = nrr, nri, nrj, nbi, nbj
            if flag:
                ans = min(i + 1, ans)
                break
            if blue_in:
                break
        return
    for j in range(len(di)):
        if n:
            if (j + 2) % 4 == tlst[n - 1]: continue
            if j == tlst[n - 1]: continue
            dfs(n + 1, tlst + [j])
        else:
            dfs(n + 1, tlst + [j])


N, M = map(int, input().split())
arr_o = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr_o[i][j] == 'O':
            hall = (i, j)
        elif arr_o[i][j] == 'R':
            red = (i, j)
            arr_o[i][j] = '.'
        elif arr_o[i][j] == 'B':
            blue = (i, j)
            arr_o[i][j] = '.'

ans = 21e8
dfs(0, [])
print(-1 if ans == 21e8 else ans)