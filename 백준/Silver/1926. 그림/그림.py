'''
Memo Boj 1926 그림
'''

from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(i, j):
    global ans
    if arr[i][j] == 0 or v[i][j] == 1:
        return 0
    q = deque()
    q.append((i, j))
    v[i][j] = 1
    time = 1
    tmp = 1
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] == 1:
                v[ni][nj] = 1
                q.append((ni, nj))
                tmp += 1
        ans = max(ans,tmp)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0 for _ in range(M)] for _ in range(N)]
cnt = 0  # 그림의 개수
ans = 0  # 가장 넓은 그림의 넓이
for i in range(N):
    for j in range(M):
        if bfs(i, j) != 0:
            cnt += 1

print(cnt)
print(ans)