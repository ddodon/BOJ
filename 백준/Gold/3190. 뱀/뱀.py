from collections import deque, defaultdict

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
for _ in range(K):
    # 사과 위치
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    arr[x][y] = 1
L = int(input())
dir = defaultdict(int)
time_to_turn = set()
for _ in range(L):
    # 뱀 방향 변환 정보
    X, C = input().split()
    X = int(X)
    dir[X] = C
    time_to_turn.add(X)

# 뱀,
snake = deque()
ci = cj = 0
snake.append((ci, cj))

# 종료 때 까지 이동
time = d = 0
while 1:
    time += 1

    # 1. 뱀이 한 칸 전진
    ni = ci + di[d]
    nj = cj + dj[d]

    # 2-1. 벽 / 본인이면 종료
    if not (0 <= ni < N and 0 <= nj < N) or (ni, nj) in snake:
        break
    snake.appendleft((ni, nj))
    # 2-2. 사과가 없다
    if arr[ni][nj] == 0:
        snake.pop()
    # 2-3. 사과가 있으면 먹기
    elif arr[ni][nj] == 1:
        arr[ni][nj]=0

    # 3. 회전 할 시간인지 체크
    if time in time_to_turn:
        # 시계 방향
        if dir[time] == 'D':
            d = (d + 1) % 4
        # 반시계 방향
        else:
            d = (d - 1) % 4
    ci, cj = ni, nj
print(time)