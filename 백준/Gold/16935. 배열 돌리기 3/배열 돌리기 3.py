def cal_1(arr):
    N = len(arr)
    M = len(arr[0])
    nrr = [[0] * M for _ in range(N)]
    for i in range(N):
        nrr[i] = arr[N - 1 - i]
    return nrr


def cal_2(arr):
    N = len(arr)
    M = len(arr[0])
    nrr = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            nrr[i][j] = arr[i][M - 1 - j]
    return nrr


def cal_3(arr):
    N = len(arr)
    M = len(arr[0])
    # nrr = [list(lst) for lst in zip(*arr[::-1])]
    nrr = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            nrr[i][j] = arr[N - 1 - j][i]
    return nrr


def cal_4(arr):
    N = len(arr)
    M = len(arr[0])
    # nrr = [list(lst) for lst in zip(*arr)][::-1]
    nrr = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            nrr[i][j] = arr[j][M - 1 - i]
    return nrr


def cal_5(arr):
    N = len(arr)
    M = len(arr[0])
    nrr = [[0] * M for _ in range(N)]
    for i in range(N // 2):
        for j in range(M // 2):
            nrr[i][j + M // 2] = arr[i][j]

    for i in range(N // 2):
        for j in range(M // 2, M):
            nrr[i + N // 2][j] = arr[i][j]

    for i in range(N // 2, N):
        for j in range(M // 2, M):
            nrr[i][j - M // 2] = arr[i][j]

    for i in range(N // 2, N):
        for j in range(M // 2):
            nrr[i - N // 2][j] = arr[i][j]
    return nrr


def cal_6(arr):
    N = len(arr)
    M = len(arr[0])
    nrr = [[0] * M for _ in range(N)]
    for i in range(N // 2):
        for j in range(M // 2):
            nrr[i + N // 2][j] = arr[i][j]

    for i in range(N // 2):
        for j in range(M // 2, M):
            nrr[i][j - M // 2] = arr[i][j]

    for i in range(N // 2, N):
        for j in range(M // 2, M):
            nrr[i - N // 2][j] = arr[i][j]

    for i in range(N // 2, N):
        for j in range(M // 2):
            nrr[i][j + M // 2] = arr[i][j]
    return nrr


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

for order in orders:
    if order == 1:
        arr = cal_1(arr)
    elif order == 2:
        arr = cal_2(arr)
    elif order == 3:
        arr = cal_3(arr)
    elif order == 4:
        arr = cal_4(arr)
    elif order == 5:
        arr = cal_5(arr)
    else:
        arr = cal_6(arr)
for x in arr:
    print(*x)