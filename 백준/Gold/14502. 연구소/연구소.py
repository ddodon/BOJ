'''
Memo Boj 14502 연구소
시도 1)
빈칸 좌표 - 세 벽 놓을 좌표 조합 - 조합마다 BFS - 최대 안전영역
'''

from itertools import combinations
from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    global tmp
    q = deque()
    q.append((i, j))
    v[i][j] = 1
    while q:
        ci, cj = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and v[ni][nj] == 0: # 빈 칸이고, 미방문
                    v[ni][nj] = 1
                    # tmp -= 1
                    # if tmp < mx:
                    #     return
                    q.append((ni, nj))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
# 1. 빈칸 좌표
blank = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            blank.append((i, j))
            cnt += 1
cnt -= 3  # 벽 3개
# 2. 빈칸 좌표 조합
wall_ok = list(combinations(blank, 3))
mx = 0  # 최대 안전 영역 개수
for ok in wall_ok:
    tmp = cnt
    ans = 0
    v = [[0 for _ in range(M)] for _ in range(N)]
    wall_1, wall_2, wall_3 = ok
    w1_i, w1_j = wall_1
    w2_i, w2_j = wall_2
    w3_i, w3_j = wall_3
    v[w1_i][w1_j] = 1
    v[w2_i][w2_j] = 1
    v[w3_i][w3_j] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2 and v[i][j] == 0:
                bfs(i, j)
    for i in range(N):
        for j in range(M):
            if v[i][j] == 0 and arr[i][j] == 0:
                ans += 1
    mx = max(mx, ans)
print(mx)