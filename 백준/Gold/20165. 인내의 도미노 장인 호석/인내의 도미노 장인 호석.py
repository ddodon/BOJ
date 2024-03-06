from collections import deque

# 동 서 남 북
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def attack(i, j, d):
    global cnt
    if (not (0 <= i < N and 0 <= j < M)) or v[i][j] == 'F':
        return

    if d == 'E':
        cnt += wave(i, j, 0)
    elif d == 'W':
        cnt += wave(i, j, 1)
    elif d == 'S':
        cnt += wave(i, j, 2)
    elif d == 'N':
        cnt += wave(i, j, 3)


def up(i, j):
    global cnt
    if (not (0 <= i < N and 0 <= j < M)) or v[i][j] == 'S':
        return
    else:
        v[i][j] = 'S'


def wave(i, j, k):
    q = deque()
    q.append((i, j))
    v[i][j] = 'F'
    cnt = 1
    while q:
        ci, cj = q.popleft()
        power = arr[ci][cj]
        for p in range(1, power):
            ni = ci + di[k] * p
            nj = cj + dj[k] * p
            if 0 <= ni < N and 0 <= nj < M:
                if v[ni][nj] == 'S':
                    v[ni][nj] = 'F'
                    cnt += 1
                    q.append((ni, nj))
    return cnt


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [['S'] * M for _ in range(N)]
cnt = 0
for _ in range(R):
    # 공격
    X, Y, D = input().split()
    X, Y = map(int, (X, Y))
    X, Y = X - 1, Y - 1
    attack(X, Y, D)

    # print("공격:", cnt)
    # for lst in v:
    #     print(*lst)
    # print("////////////////")

    # 수비
    X, Y = map(int, input().split())
    X, Y = X - 1, Y - 1
    up(X, Y)

    # print("수비")
    # for lst in v:
    #     print(*lst)
    # print("////////////////")

print(cnt)
for lst in v:
    print(*lst)
