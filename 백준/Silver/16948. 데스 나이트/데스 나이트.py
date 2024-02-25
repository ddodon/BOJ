from collections import deque

di = [-2, -2, 0, 0, 2, 2]
dj = [-1, 1, -2, 2, -1, 1]


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    arr[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (r2, c2):
            print(arr[ci][cj] - 1)
            break
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                arr[ni][nj] = arr[ci][cj] + 1
                q.append((ni, nj,))
    else:
        print(-1)


N = int(input())
r1, c1, r2, c2 = map(int, input().split())
arr = [[0] * N for _ in range(N)]

bfs(r1, c1)