from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj, num):
    q = deque()
    q.append((si, sj))
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if (0 <= ni < N and 0 <= nj < M) and v[ni][nj] == 0 and arr[ni][nj] == B:
                q.append((ni, nj))
                v[ni][nj] = 1
                cnt += 1
    return cnt


def dice(lst, d):
    Back, Left, Up, Right, Front, Down = lst
    if d == 0:
        lst = [Up,Left,Front,Right,Down,Back]
    elif d == 1:
        lst = [Back,Down,Left,Up,Front,Right]
    elif d == 2:
        lst = [Down,Left,Back,Right,Up,Front]
    else:
        lst = [Back,Up,Right,Down,Front,Left]
    return lst


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = [2, 4, 1, 3, 5, 6]
d = 1
ci = cj = 0
ans = 0
for _ in range(K):
    ni = ci + di[d]
    nj = cj + dj[d]
    if not (0 <= ni < N and 0 <= nj < M):
        d = (d + 2) % 4
        ni = ci + di[d]
        nj = cj + dj[d]
    lst = dice(lst, d)
    A = lst[5]
    B = arr[ni][nj]
    if A > B:
        d = (d + 1) % 4
    elif A < B:
        d = (d - 1) % 4
    C = bfs(ni, nj, B)
    ans += B * C
    ci, cj = ni, nj
print(ans)