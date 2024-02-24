'''
Memo 21938 영상처리
결과 1) x
bfs 내 while문에서
while q: 를 while 1: 이라고 적는 쓰레기같은 실수를 했다.
'''
import sys
from collections import deque

# 방향
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] == 255:
                v[ni][nj] = 1
                q.append((ni, nj))


N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]
v = [[0] * M for _ in range(N)]
tmp = [list(map(int, input().split())) for _ in range(N)]
T = int(input())
for i in range(N):
    for j in range(0, 3 * M, 3):
        if T <= (tmp[i][j] + tmp[i][j + 1] + tmp[i][j + 2]) // 3:
            arr[i][j // 3] = 255
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 255 and v[i][j] == 0:
            cnt += 1
            bfs(i,j)
print(cnt)