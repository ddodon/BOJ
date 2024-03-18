# 총 시간: 분
# 문제 읽기: 0:14:00 ~ 0:23:00
# 풀이 구상:
# 로직 구현:
# 오류 수정:  ~ 2:02:40
# 제출 결과: (/2)
# 오류 부분: 말 변수의 좌표가 고정되어 있었음, 말이 한꺼번에 이동할 때 말 좌표 안바뀜,indexerror, chess배열 생성시 K개 만큼 만들었따...

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]


def move(ci, cj, d, horse):
    idx = chess[ci][cj].index(horse)
    ni = ci + di[d]
    nj = cj + dj[d]
    if 0 <= ni < N and 0 <= nj < N and color[ni][nj] != Blue:
        if color[ni][nj] == White:
            chess[ni][nj] += chess[ci][cj][idx:]
            chess[ci][cj] = chess[ci][cj][:idx]
        elif color[ni][nj] == Red:
            chess[ni][nj] += chess[ci][cj][idx:][::-1]
            chess[ci][cj] = chess[ci][cj][:idx]
    else:
        if d == 0:
            d = 1
        elif d == 1:
            d = 0
        elif d == 2:
            d = 3
        elif d == 3:
            d = 2
        ni = ci + di[d]
        nj = cj + dj[d]
        if (0 <= ni < N and 0 <= nj < N) and color[ni][nj] != Blue:
            if color[ni][nj] == White:
                chess[ni][nj] += chess[ci][cj][idx:]
                chess[ci][cj] = chess[ci][cj][:idx]
            elif color[ni][nj] == Red:
                chess[ni][nj] += chess[ci][cj][idx:][::-1]
                chess[ci][cj] = chess[ci][cj][:idx]
        else:
            ni, nj = ci, cj
    return (ni, nj, d)


def check():
    for i in range(N):
        for j in range(N):
            if len(chess[i][j]) >= 4:
                return True
    return False


White, Red, Blue = 0, 1, 2
N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]
chess = [[[] for _ in range(N)] for _ in range(N)]
order = []
for k in range(1, K + 1):
    r, c, d = map(int, input().split())
    chess[r - 1][c - 1].append(k)
    order.append([r - 1, c - 1, d - 1])
ans = 0

flag = True
while flag:
    ans += 1
    if ans > 1000:
        break
    for i in range(K):
        cr, cc, cd = order[i][0], order[i][1], order[i][2]
        (nr, nc, nd) = move(order[i][0], order[i][1], order[i][2], i + 1)
        order[i][0], order[i][1], order[i][2] = nr, nc, nd
        for h in chess[nr][nc]:
            if h == 0: continue
            order[h - 1][0], order[h - 1][1] = nr, nc
        res = check()
        if res:
            flag = False
            break
print(-1 if ans > 1000 else ans)