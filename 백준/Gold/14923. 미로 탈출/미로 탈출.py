from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj):
    q = deque()
    magic = 0
    q.append((si, sj, magic))
    v = [[[0, 0] for _ in range(M)] for _ in range(N)]
    v[si][sj][magic] = 1
    while q:
        ci, cj, cmagic = q.popleft()
        if (ci, cj) == (Ex, Ey):
            return v[ci][cj][cmagic] - 1
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1 and v[ni][nj][cmagic] == 0:
                q.append((ni, nj, cmagic))
                v[ni][nj][cmagic] = v[ci][cj][cmagic] + 1
        if cmagic < 1:
            for k in range(len(di)):
                ni = ci + di[k]
                nj = cj + dj[k]
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and v[ni][nj][cmagic] == 0:
                    q.append((ni, nj, cmagic + 1))
                    v[ni][nj][cmagic + 1] = v[ci][cj][cmagic] + 1
    return - 1


N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())
Hx, Hy, Ex, Ey = Hx - 1, Hy - 1, Ex - 1, Ey - 1
arr = [list(map(int, input().split())) for _ in range(N)]
ans = bfs(Hx, Hy)
print(ans)