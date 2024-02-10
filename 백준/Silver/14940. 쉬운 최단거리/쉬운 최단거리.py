'''
Memo BOJ 14940 쉬운 최단거리
BFS visited 배열에 최단거리 삽입
'''
from collections import deque

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    v[i][j] = 0

    while q:
        ci, cj = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            # 범위 내 + 가본 적 없는 곳 + 0이 아닌 곳 + 갈 수 있는 곳
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] == 1:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            si, sj = i, j
            break
bfs(si, sj)

# 갈 수 있는 길이지만 가지 못한 곳
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and v[i][j] == 0:
            v[i][j] = -1
# 출발좌표
v[si][sj] = 0
for lst in v:
    print(*lst)