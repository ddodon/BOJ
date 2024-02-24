from collections import deque

# 8방향
di = [-1, -1, 0, 1, 1, 1, -1, 0]
dj = [0, 1, 1, 1, 0, -1, -1, -1]


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < M and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj]:
                v[ni][nj] = 1
                q.append((ni, nj))


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
v = [[0] * N for _ in range(M)]

cnt = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] and v[i][j] == 0:
            cnt += 1
            bfs(i, j)
print(cnt)