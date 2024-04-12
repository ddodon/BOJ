from collections import deque


def turn(arr, R):
    mx_depth = min(N, M) // 2  # 최대 깊이
    ci, cj = 0, 0
    for t in range(mx_depth):
        q = deque()
        for j in range(cj, M - t):
            q.append(arr[ci][j])
        for i in range(ci + 1, N - t - 1):
            q.append((arr[i][M - t - 1]))
        for j in range(ci, M - t)[::-1]:
            q.append(arr[N - t - 1][j])
        for i in range(ci + 1, N - t - 1)[::-1]:
            q.append(arr[i][cj])

        q.rotate(-(R % len(q)))

        for j in range(cj, M - t):
            arr[ci][j] = q.popleft()
        for i in range(ci + 1, N - t - 1):
            arr[i][M - t - 1] = q.popleft()
        for j in range(ci, M - t)[::-1]:
            arr[N - t - 1][j] = q.popleft()
        for i in range(ci + 1, N - t - 1)[::-1]:
            arr[i][cj] = q.popleft()
        ci, cj = ci + 1, cj + 1
    return arr


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = turn(arr, R)
for lst in arr:
    print(*lst)