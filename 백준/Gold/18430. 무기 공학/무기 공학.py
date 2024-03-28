def dfs(r,c,sm):
    global ans
    ans = max(ans, sm)

    for i in range(r,N):
        for j in range(c,M):
            if v[i][j] == 0:
                for k in range(len(dir)):
                    (di, dj), (fi, fj) = dir[k]
                    if 0 <= i + di < N and 0 <= i + fi < N and 0 <= j + dj < M and 0 <= j + fj < M:
                        if v[i + di][j + dj] == 0 and v[i + fi][j + fj] == 0:
                            v[i][j] = 1
                            v[i + di][j + dj] = 1
                            v[i + fi][j + fj] = 1
                            dfs(i-1,j-1, sm + ((arr[i][j]) * 2 + arr[i + di][j + dj] + arr[i + fi][j + fj]))
                            v[i][j] = 0
                            v[i + di][j + dj] = 0
                            v[i + fi][j + fj] = 0


dir = [[(-1, 0), (0, 1)], [(-1, 0), (0, -1)], [(1, 0), (0, 1)], [(1, 0), (0, -1)]]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
ans = -21e8
dfs(0, 0,0)
print(ans)