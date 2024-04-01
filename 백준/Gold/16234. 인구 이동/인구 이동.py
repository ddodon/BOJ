# BFS 함수 호출 유무 시간 비교

from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
day = 0

q = deque()
while 1:
    cnt = 0
    v = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                q.append((i, j))
                v[i][j] = 1
                union = [(i, j)]
                while q:
                    ci, cj = q.popleft()
                    for k in range(len(di)):
                        ni = ci + di[k]
                        nj = cj + dj[k]
                        if 0 <= ni < N and 0 <= nj < N:
                            if v[ni][nj] == 0 and (L <= abs(arr[ci][cj] - arr[ni][nj]) <= R):
                                q.append((ni, nj))
                                v[ni][nj] = 1
                                union.append((ni, nj))
                div = len(union)
                if div > 1:
                    sm = 0
                    for (ui, uj) in union:
                        sm += arr[ui][uj]
                    for (ui, uj) in union:
                        arr[ui][uj] = sm // div
                    cnt = 1
    if cnt == 0:
        break
    else:
        day += 1
print(day)