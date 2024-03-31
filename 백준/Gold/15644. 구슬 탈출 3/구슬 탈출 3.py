di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def tilt(red_ball, blue_ball, arr, d):
    red_in = False
    blue_in = False
    ri, rj = red_ball
    bi, bj = blue_ball

    # 빨간공 먼저
    while 1:
        ni = ri + di[d]
        nj = rj + dj[d]
        if arr[ni][nj] == '.':  # 다음 칸이 빈칸
            arr[ri][rj], arr[ni][nj] = arr[ni][nj], arr[ri][rj]
            ri, rj = ni, nj
        elif arr[ni][nj] == '#' or arr[ni][nj] == 'B':  # 다음 칸이 벽/구슬
            break
        elif arr[ni][nj] == 'O':  # 다음 칸이 구멍
            arr[ri][rj] = '.'
            ri, rj = ni, nj
            red_in = True
            break

    # 파란공 굴리기
    while 1:
        ni = bi + di[d]
        nj = bj + dj[d]
        if arr[ni][nj] == '.':  # 다음 칸이 빈칸
            arr[bi][bj], arr[ni][nj] = arr[ni][nj], arr[bi][bj]
            bi, bj = ni, nj
        elif arr[ni][nj] == '#' or arr[ni][nj] == 'R':  # 다음 칸이 벽/구슬
            break
        elif arr[ni][nj] == 'O':  # 다음 칸이 구멍
            arr[bi][bj] = '.'
            bi, bj = ni, nj
            blue_in = True
            return (blue_in, False, (ri, rj), (bi, bj), arr)
            break

    # 다시 빨간공
    while 1:
        ni = ri + di[d]
        nj = rj + dj[d]

        if arr[ni][nj] == '.':  # 다음 칸이 빈칸
            arr[ri][rj], arr[ni][nj] = arr[ni][nj], arr[ri][rj]
            ri, rj = ni, nj
        elif arr[ni][nj] == '#' or arr[ni][nj] == 'B':  # 다음 칸이 벽/구슬
            break
        elif arr[ni][nj] == 'O':  # 다음 칸이 구멍
            arr[ri][rj] = '.'
            ri, rj = ni, nj
            red_in = True
            break
    return (blue_in, red_in, (ri, rj), (bi, bj), arr)


def dfs(n, orders):
    global ans
    # 무한루프? ->
    if n == 10:
        r_ball, b_ball = red_ball, blue_ball
        nrr = [lst[::] for lst in arr]
        for t, order in enumerate(orders):
            if t + 1 > ans:
                return
            blue_in, red_in, r_ball, b_ball, nrr = tilt(r_ball, b_ball, nrr, order)
            if blue_in:
                return
            if red_in:
                ans = min(ans, t + 1)
                route.append(orders)
                return
        return

    for j in range(len(di)):
        if orders and (orders[-1] == j or orders[-1] == (j + 2) % 4):
            continue
        dfs(n + 1, orders + [j])


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
# 최소 공 개수
ans = 21e8
route = []
# 색깔별 공 위치
for i in range(1,N-1):
    for j in range(1,M-1):
        if arr[i][j] == 'R':
            red_ball = (i, j)
        elif arr[i][j] == 'B':
            blue_ball = (i, j)

# 백트래킹
dfs(0, [])
dir = {0:'U',1:'R',2:'D',3:'L'}
if ans == 21e8:
    print(-1)
else:
    print(ans)
    for order in route[-1][:ans]:
        print(dir[order],end="")