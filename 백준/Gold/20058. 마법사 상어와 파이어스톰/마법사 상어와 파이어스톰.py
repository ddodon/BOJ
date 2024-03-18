# 좌표기준 for문 전치행렬
from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def check(i, j):
    cnt = 0
    for k in range(len(di)):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N and arr[ni][nj] > 0:
            cnt += 1
    if cnt < 3:
        return (i, j)

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N and arr[ni][nj] > 0 and v[ni][nj] == 0:
                cnt += 1
                q.append((ni, nj))
                v[ni][nj] = 1
    return cnt

N, Q = map(int, input().split())
arr_b = [list(map(int, input().split())) for _ in range(2 ** N)]

v = [[0] * (2 ** N) for _ in range(2 ** N)]
ans1 = 0
ans2 = 0
qq = list(map(int, input().split()))

for q in qq:
    q = 2 ** q
    arr = [[0] * (2 ** N) for _ in range(2 ** N)]
    for si in range(0, 2 ** N, q):
        for sj in range(0, 2 ** N, q):
            for i in range(q):
                for j in range(q):
                    arr[si+i][sj+j] = arr_b[si+q-1-j][sj+i]

    non_ice = []
    for i in range(2 ** N):
        for j in range(2 ** N):
            non_ice.append(check(i, j))
    for loc in non_ice:
        if loc:
            ci, cj = loc
            arr[ci][cj] -= 1
    arr_b = arr

for i in range(2 ** N):
    for j in range(2 ** N):
        if arr[i][j] > 0 and v[i][j] == 0:
            ans2 = max(ans2, bfs(i, j))
        if arr[i][j] > 0:
            ans1 += arr[i][j]

print(ans1)
print(ans2)