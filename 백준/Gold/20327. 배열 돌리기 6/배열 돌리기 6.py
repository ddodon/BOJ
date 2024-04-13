def cal(arr, k, L):
    nrr = [[0] * N for _ in range(N)]

    if k == 1:
        for si in range(0, N, L):
            for sj in range(0, N, L):
                for i in range(L):
                    for j in range(L):
                        nrr[si + i][sj + j] = arr[si + L - i - 1][sj + j]
    elif k == 2:
        for si in range(0, N, L):
            for sj in range(0, N, L):
                for i in range(L):
                    for j in range(L):
                        nrr[si + i][sj + j] = arr[si + i][sj + L - j - 1]

    elif k == 3:
        for si in range(0, N, L):
            for sj in range(0, N, L):
                for i in range(L):
                    for j in range(L):
                        nrr[si + i][sj + j] = arr[si + L - j - 1][sj + i]
    elif k == 4:
        for si in range(0, N, L):
            for sj in range(0, N, L):
                for i in range(L):
                    for j in range(L):
                        nrr[si + i][sj + j] = arr[si + j][sj + L - i - 1]

    elif k == 5:
        box = [[] for _ in range((N * N) // (L * L))]
        cnt = 0
        for si in range(0, N, L):
            for sj in range(0, N, L):
                for i in range(L):
                    for j in range(L):
                        box[cnt].append(arr[si + i][sj + j])
                cnt += 1
        cnt = -1
        box = box[::-1]
        for si in range(N - L, -1, -L):
            for sj in range(0, N, L):
                for i in range(L):
                    for j in range(L):
                        nrr[si + i][sj + j] = box[cnt].pop(0)
                cnt -= 1
    elif k == 6:
        box = [[] for _ in range((N * N) // (L * L))]
        cnt = 0
        for si in range(0, N, L):
            for sj in range(0, N, L):
                for i in range(L):
                    for j in range(L):
                        box[cnt].append(arr[si + i][sj + j])
                cnt += 1
        cnt = 0
        for si in range(0, N, L):
            for sj in range(N - L, -1, -L):
                for i in range(L):
                    for j in range(L):
                        nrr[si + i][sj + j] = box[cnt].pop(0)
                cnt += 1
    elif k == 7:
        trr = [list(lst) for lst in zip(*arr[::-1])]
        for si in range(0, N, L):
            for sj in range(0, N, L):
                for i in range(L):
                    for j in range(L):
                        nrr[si + i][sj + j] = trr[si + j][sj + L - i - 1]
    elif k == 8:
        trr = [list(lst) for lst in zip(*arr)][::-1]
        for si in range(0, N, L):
            for sj in range(0, N, L):
                for i in range(L):
                    for j in range(L):
                        nrr[si + i][sj + j] = trr[si + L - j - 1][sj + i]

    return nrr


n, R = map(int, input().split())
N = 2 ** n
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(R):
    k, l = map(int, input().split())
    L = 2 ** l
    arr = cal(arr, k, L)
for x in arr:
    print(*x)