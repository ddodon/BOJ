import sys
sys.setrecursionlimit(100000)
# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(j, i):
    if v[i][j] == 0:
        return 0
    v[i][j] = 0

    for k in range(4):  # 4방향
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 1:  # 범위 내 + 근처에 배추가 있나!
            if v[ni][nj] == 1:
                dfs(nj, ni)
            else:
                continue
        else:
            continue
    return 1
TC = int(input())
for tc in range(TC):
    M, N, K = map(int, input().split())
    adj = [[] for _ in range(N * M)]
    ans = [[]]
    v = [[0] * (M) for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        v[y][x] = 1
    ans = 0
    for i in range(M):
        for j in range(N):
            if dfs(i, j) != 0:
                ans += 1
    print(ans)