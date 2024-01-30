import sys
sys.setrecursionlimit(100000) # ㅡ..ㅡ
# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
global ans #전역변수) 영역별 사각형 넓이
def dfs(i,j):
    if table[i][j] == 1:
        return 0
    table[i][j] = 1
    global ans
    for k in range(4):  # 4방향
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < M and 0 <= nj < N and table[ni][nj] == 0: #
            if table[ni][nj] == 0:
                dfs(ni, nj)
                ans += 1
            else:
                continue
        else:
            continue
    return ans

M, N, K = map(int, input().split())
table = [[0]*(N) for _ in range(M)]

for i in range(K):
    xi, xj, yi, yj = map(int,input().split())
    for a in range(xj,yj):
        for b in range(xi,yi):
            table[a][b] = 1

cnt = 0
res = []
for j in range(N):
    for i in range(M-1,-1,-1):
        ans = 1
        if dfs(i,j) != 0:
            cnt += 1
            res.append(ans)
print(cnt)
res.sort() # 크기 순으로 정렬 해주기
print(*res)