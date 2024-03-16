from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (fr, fc):
            return v[ci][cj] - 1
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni <= N - H and 0 <= nj <= M - W and v[ni][nj] == 0 and arr[ni][nj] == 0:
                if check(ni, nj):
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj] + 1
    return -1


def check(i, j):
    for wi, wj in wall:
        if i <= wi < i + H and j <= wj < j + W:
            return False
    return True


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
H, W, sr, sc, fr, fc = map(int, input().split())
sr, sc, fr, fc = sr - 1, sc - 1, fr - 1, fc - 1
wall = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            wall.append((i, j))
ans = bfs(sr, sc)
print(ans)