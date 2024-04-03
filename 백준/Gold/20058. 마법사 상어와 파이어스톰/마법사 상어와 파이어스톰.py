from collections import deque


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
            if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N and v[ni][nj] == 0 and arr[ni][nj] > 0:
                q.append((ni, nj))
                v[ni][nj] = 1
                cnt += 1
    return cnt


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def melt(arr):
    nrr = [lst[::] for lst in arr]
    for i in range(2 ** N):
        for j in range(2 ** N):
            cnt = 0
            if arr[i][j] <= 0: continue
            ci, cj = i, j
            for k in range(len(di)):
                ni = ci + di[k]
                nj = cj + dj[k]
                if not (0 <= ni < 2 ** N and 0 <= nj < 2 ** N) or arr[ni][nj] == 0:
                    continue
                else:
                    cnt += 1
            if cnt < 3:
                nrr[ci][cj] -= 1
    return nrr


N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2 ** N)]
order = list(map(int, input().split()))  # 마법 횟수

for q in range(Q):
    L = 2 ** order[q]
    # 1. 부분 회전
    nrr = [lst[::] for lst in arr]
    for si in range(0, 2 ** N, L):
        for sj in range(0, 2 ** N, L):
            for i in range(L):
                for j in range(L):
                    arr[si + i][sj + j] = nrr[si + L - 1 - j][sj + i]

    # 2. 얼음 녹이기
    arr = melt(arr)

v = [[0] * (2 ** N) for _ in range(2 ** N)]
mx = 0
for i in range(2 ** N):
    for j in range(2 ** N):
        if arr[i][j] > 0 and v[i][j] == 0:
            res = bfs(i, j)
            mx = max(res, mx)
print(sum(map(sum, arr)))
print(mx)