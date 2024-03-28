di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def dfs(n, sm, tlst):
    global ans
    if ans >= sm + (4 - n) * mx:
        return
    if n == 4:
        ans = max(sm, ans)
        return

    for ci, cj in tlst:
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0:
                v[ni][nj] = 1
                dfs(n + 1, sm + arr[ni][nj], tlst + [(ni, nj)])
                v[ni][nj] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
mx = max(map(max, arr))
ans = 0
for i in range(N):
    for j in range(M):
        v[i][j] = 1
        dfs(1, arr[i][j], [(i, j)])
print(ans)