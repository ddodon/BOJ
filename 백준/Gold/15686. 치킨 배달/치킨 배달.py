from itertools import combinations

def cal(h, c):
    sm = 0
    for hi, hj in h:
        mn = 21e8
        for ci, cj in c:
            mn = min(mn, (abs(ci - hi) + abs(cj - hj)))
        sm += mn
    return sm

# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 집 / 치킨 좌표
H = []
C = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            H.append((i, j))
        elif arr[i][j] == 2:
            C.append((i, j))
            arr[i][j] = 0

Chick = list(combinations(C, M))

# 치킨집 삭제
mn_dist = 100000
for chick in Chick:
    mn_dist = min(mn_dist, cal(H, chick))
print(mn_dist)