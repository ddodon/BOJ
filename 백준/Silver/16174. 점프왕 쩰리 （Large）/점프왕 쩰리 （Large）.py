from collections import deque

di = [0, 1]
dj = [1, 0]


def bfs(si, sj):
    q = deque()
    q.append((si, sj, arr[si][sj]))
    v[si][sj] = 1
    while q:
        ci, cj, t = q.popleft()
        if arr[ci][cj] == -1:
            print("HaruHaru")
            break
        for k in range(len(di)):
            ni = ci + di[k] * t
            nj = cj + dj[k] * t
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                v[ni][nj] = 1
                q.append((ni, nj, arr[ni][nj]))
    else:
        print('Hing')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]

bfs(0, 0)