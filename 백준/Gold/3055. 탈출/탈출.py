from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v = [[0] * C for _ in range(R)]
    v[si][sj] = 1
    for wi, wj in water:
        v[wi][wj] = -1
    water_q = deque(water)
    while q:
        for i in range(len(water_q)):
            wi, wj = water_q.popleft()
            for k in range(len(di)):
                nwi = wi + di[k]
                nwj = wj + dj[k]
                if 0 <= nwi < R and 0 <= nwj < C and arr[nwi][nwj] != 'X' and v[nwi][nwj] == 0:
                    if arr[nwi][nwj] != 'D':
                        water_q.append((nwi, nwj))
                        v[nwi][nwj] = v[wi][wj] - 1

        for i in range(len(q)):
            ci, cj = q.popleft()
            for k in range(len(di)):
                ni = ci + di[k]
                nj = cj + dj[k]
                if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != 'X' and v[ni][nj] == 0:
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj] + 1
    return v[ei][ej] - 1


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
water = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'D':
            ei, ej = i, j
        elif arr[i][j] == 'S':
            si, sj = i, j
        elif arr[i][j] == '*':
            water.append((i, j))
ans = bfs(si, sj)
print("KAKTUS" if ans < 1 else ans)