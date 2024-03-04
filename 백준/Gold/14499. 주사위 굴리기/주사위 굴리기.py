di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def turn(dice, c):
    tlst = dice[:]
    if c == 1:#동
        tlst[0] = dice[3]
        tlst[2] = dice[0]
        tlst[3] = dice[5]
        tlst[5] = dice[2]
    elif c == 2:#서
        tlst[0] = dice[2]
        tlst[2] = dice[5]
        tlst[3] = dice[0]
        tlst[5] = dice[3]
    elif c == 3:#북
        tlst[0] = dice[4]
        tlst[1] = dice[0]
        tlst[4] = dice[5]
        tlst[5] = dice[1]
    elif c == 4:#남
        tlst[0] = dice[1]
        tlst[1] = dice[5]
        tlst[4] = dice[0]
        tlst[5] = dice[4]
    return tlst
# 입력
N, M, ci, cj, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
dice = [0,0,0,0,0,0]
for c in command:
    ni = ci + di[c - 1]
    nj = cj + dj[c - 1]
    if not (0 <= ni < N and 0 <= nj < M):
        continue
    ci, cj = ni, nj
    dice = turn(dice, c)
    print(dice[0])
    if arr[ci][cj] == 0:
        arr[ci][cj] = dice[5]
    else:
        dice[5] = arr[ci][cj]
        arr[ci][cj] = 0