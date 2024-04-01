from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def spread(arr):
    nrr = [lst[::] for lst in arr]
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                ci, cj = i, j
                for k in range(len(di)):
                    ni = ci + di[k]
                    nj = cj + dj[k]
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        nrr[ni][nj] += arr[ci][cj] // 5
                        nrr[ci][cj] -= arr[ci][cj] // 5
    return nrr


def wind(arr):
    # up
    up_side = deque()
    u, d = up[0], down[0]
    for j in range(1, C):
        up_side.append(arr[u][j])
    for i in range(u - 1, 0, -1):
        up_side.append(arr[i][C - 1])
    for j in range(C - 1, -1, -1):
        up_side.append(arr[0][j])
    for i in range(1, u):
        up_side.append(arr[i][0])

    # 정화
    up_side.pop()
    up_side.appendleft(0)

    for j in range(1, C):
        arr[u][j] = up_side.popleft()
    for i in range(u - 1, 0, -1):
        arr[i][C - 1] = up_side.popleft()
    for j in range(C - 1, -1, -1):
        arr[0][j] = up_side.popleft()
    for i in range(1, u):
        arr[i][0] = up_side.popleft()

    # down
    down_side = deque()
    for i in range(1, C):
        down_side.append(arr[d][i])
    for i in range(d + 1, R - 1):
        down_side.append(arr[i][C - 1])
    for i in range(C - 1, -1, -1):
        down_side.append(arr[R - 1][i])
    for i in range(R - 2, d, -1):
        down_side.append(arr[i][0])
    down_side.appendleft(0)
    down_side.pop()
    for i in range(1, C):
        arr[d][i] = down_side.popleft()
    for i in range(d + 1, R - 1):
        arr[i][C - 1] = down_side.popleft()
    for i in range(C - 1, -1, -1):
        arr[R - 1][i] = down_side.popleft()
    for i in range(R - 2, d, -1):
        arr[i][0] = down_side.popleft()
    return arr


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
for i in range(R):
    if arr[i][0] == -1:
        up = (i, 0)
        down = (i + 1, 0)
        break

for t in range(T):
    # 1. 미세먼지 확산
    arr = spread(arr)
    # 2. 공기청정기 작동
    arr = wind(arr)

print(sum(map(sum, arr)) + 2)