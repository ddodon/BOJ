'''
Memo BOJ 2636 치즈
* 몇번째 방문인지 체크 (현재 위치가 치즈인데, 두번째 방문 -> 닿는 면이 2개 -> 녹임) 
'''
from collections import deque

# 방향: 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(i, j):
    q = deque()
    # i좌표, j좌표,
    q.append((i, j))
    v[i][j] = 1
    cnt = 0
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0:
                # 다음이 공기라면
                if arr[ni][nj] == 0:
                    v[ni][nj] = 1
                    q.append((ni, nj))
                # 다음이 치즈라면
                else:
                    # 첫번째 방문 (닿는 면이 1개)
                    if air[ni][nj] == 0:
                        air[ni][nj] = 1
                    # 두번째 방문 (닿는 면이 2개)
                    elif air[ni][nj] == 1:
                        v[ni][nj] = 1
                        arr[ni][nj] = 0  # 치즈 녹음
                        cnt += 1
    return cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 시간별 남은 치즈
ans = []

while 1:
    v = [[0] * M for _ in range(N)]
    air = [[0] * M for _ in range(N)]
    cnt = bfs(0, 0)

    # 녹일 치즈 없음
    if cnt == 0:
        break
    else:
        ans.append(cnt)

if ans:
    print(len(ans))
else:
    print(0)