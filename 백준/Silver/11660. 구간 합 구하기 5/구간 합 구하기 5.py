N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sum_arr = [[0]*(N + 2)] + [[0]*(N + 2) for _ in range(N)] + [[0] * (N + 2)]
#0으로 둘러싸기

for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum_arr[i][j] = sum_arr[i - 1][j] + sum_arr[i][j - 1] + arr[i - 1][j - 1] - sum_arr[i - 1][j - 1]
        # 누적합 배열 생성

        # for i in range(1, N + 1):
#     print(sum_arr[i])

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    a = sum_arr[x2][y2]
    b = sum_arr[x2][y1-1]
    c = sum_arr[x1-1][y2]
    d = sum_arr[x1-1][y1-1] #중복으로 빠진 부분 덧셈
    print(a-b-c+d)