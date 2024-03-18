from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1

L = int(input())
loc = ['']*10001
for _ in range(L):
    x, c = map(str, input().split())
    loc[int(x)] = c
ci = cj = 0
d = 0
time = 0
snake = deque()
snake.append((0,0))

while 1:
    time += 1
    ni = ci + di[d]
    nj = cj + dj[d]

    if 0 <= ni < N and 0 <= nj < N and (ni,nj) not in snake:
        snake.appendleft((ni,nj))

        if arr[ni][nj] == 1:
            arr[ni][nj] = 0
        else:
            snake.pop()
        ci,cj = ni, nj
    else:
        break
    if loc[time]:
        if loc[time]=='D':
            d = (d+1)%4
        else:
            d = (d-1)%4
print(time)
