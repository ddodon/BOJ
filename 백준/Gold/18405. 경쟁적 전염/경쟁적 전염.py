di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(virus):
    virus.sort(key=lambda x: x[2])
    for ci, cj, n in virus:
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                arr[ni][nj] = n
    return arr


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

time = 0
while time != S:
    virus = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                virus.append((i, j, arr[i][j]))
    if len(virus) == N*N:
        break
    arr = bfs(virus)
    time += 1
print(arr[X - 1][Y - 1])