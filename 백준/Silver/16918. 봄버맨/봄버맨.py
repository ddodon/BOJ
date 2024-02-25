di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def new_bomb(arr, v):
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                arr[i][j] = 'O'
                v[i][j] = 3


def bomb(arr, v):
    lst = check_bomb(arr, v)
    for bi, bj in lst:
        v[bi][bj] = 'X'
        arr[bi][bj] = '.'
        for k in range(len(di)):
            ni = bi + di[k]
            nj = bj + dj[k]
            if 0 <= ni < R and 0 <= nj < C:
                v[ni][nj] = 'X'
                arr[ni][nj] = '.'


def check_bomb(arr, v):
    lst = []
    for i in range(R):
        for j in range(C):
            if v[i][j] == 0:
                lst.append((i, j))
    return lst


def time(arr, v):
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                v[i][j] -= 1


R, C, N = map(int, input().split())

arr = [list(input()) for _ in range(R)]
v = [['X'] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            v[i][j] = 2
            # 다음 1초 동안 봄버맨은 아무것도 하지 않는다
N -= 1
# 다음 1초동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다.
# 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
while N > 0:
    N -= 1
    time(arr, v)
    bomb(arr, v)
    new_bomb(arr, v)
    if N < 1:
        break

    N -= 1
    time(arr, v)
    bomb(arr, v)
    if N < 1:
        break
for lst in arr:
    print(''.join(lst))
