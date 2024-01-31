import sys
import copy
sys.setrecursionlimit(10000)

# 방향: 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dfs(i, j, v, picture, color):
    if picture[i][j] != color or v[i][j] == 1:
        return 0
    v[i][j] = 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and picture[ni][nj] == color:  # 범위 내 + v + color
            dfs(ni, nj, v, picture, color)
    return 1


N = int(input())
picture1 = [list(map(str, input())) for _ in range(N)]
picture2 = copy.deepcopy(picture1)  # 적록색약인 사람에게 보이는 그림
v1 = [[0] * N for _ in range(N)]  #
v2 = [[0] * N for _ in range(N)]  # 적록색약용 v
R = 'R'
B = 'B'
G = 'G'
cnt1 = cnt2 = 0
for i in range(N):
    for j in range(N):
        if picture1[i][j] == 'G':
            picture2[i][j] = 'R'  # 적록색약 변환

for i in range(N):
    for j in range(N):
        for k in (R, G, B):
            if dfs(i, j, v1, picture1, k) != 0:
                cnt1 += 1
for i in range(N):
    for j in range(N):
        for k in (R, B):
            if dfs(i, j, v2, picture2, k) != 0:
                cnt2 += 1
print(cnt1)
print(cnt2)