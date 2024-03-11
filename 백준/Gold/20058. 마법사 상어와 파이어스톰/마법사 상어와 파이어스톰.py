from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def trans(tmp, ci, cj):
    tmp_t = [list(lst) for lst in zip(*tmp[::-1])]
    for i in range(q):
        for j in range(q):
            arr[ci + i][cj + j] = tmp_t[i][j]


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
arr = [list(map(int, input().split())) for _ in range(2 ** N)]
arr_t = [list(lst) for lst in zip(*arr[::-1])]
v = [[0] * (2 ** N) for _ in range(2 ** N)]
ans1 = 0
ans2 = 0
qq = list(map(int, input().split()))

for l in range(Q):
    q = qq[l]
    q = 2 ** q
    for i in range(0, 2 ** N, q):
        for j in range(0, 2 ** N, q):
            tmp = []
            for lst in arr[i:i + q]:
                tmp.append(lst[j:j + q])
            trans(tmp, i, j)
    non_ice = []
    for i in range(2 ** N):
        for j in range(2 ** N):
            non_ice.append(check(i, j))
    for loc in non_ice:
        if loc:
            ci, cj = loc
            arr[ci][cj] -= 1
            
for i in range(2 ** N):
    for j in range(2 ** N):
        if arr[i][j] > 0 and v[i][j] == 0:
            ans2 = max(ans2, bfs(i, j))
        if arr[i][j] > 0:
            ans1 += arr[i][j]

print(ans1)
print(ans2)