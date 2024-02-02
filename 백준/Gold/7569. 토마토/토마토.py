from collections import deque

# 방향: 1층위, 1층아래, 상하좌우
dk = [1, -1, 0, 0, 0, 0]
di = [0, 0, -1, 1, 0, 0]
dj = [0, 0, 0, 0, -1, 1]


def bfs(arr, cnt):  # 3차원리스트
    q = deque()
    v = [[[0] * M for _ in range(N)] for _ in range(H)]
    ans = []
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[k][i][j] == 1:
                    q.append((k, i, j))
                    v[k][i][j] = 1
                    ans.append(tomato[k][i][j])
    while q:
        c = q.popleft()
        # 탈출조건
        if cnt == 0:
            return ans[-1]-1 #마지막으로 채워진 토마토의 값 - 1
        for n in range(len(di)):  # 6방향
            nk = c[0] + dk[n]
            ni = c[1] + di[n]
            nj = c[2] + dj[n]
            if 0 <= nk < H and 0 <= ni < N and 0 <= nj < M and v[nk][ni][nj] == 0 and arr[nk][ni][nj] == 0:  # 조건문
                v[nk][ni][nj] = v[c[0]][c[1]][c[2]] + 1
                q.append((nk, ni, nj))
                cnt -= 1
                ans.append(v[nk][ni][nj])
    return -1


M, N, H = map(int, input().split())
tomato = [[]] * H
for k in range(H):  # 3차원 토마토 배열
    tomato[k] = [list(map(int, input().split())) for _ in range(N)]

green = 0  # 덜익은 토마토
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 0:
                green += 1
if green == 0:
    print(0)  # 토마토가 이미 다 익음
else:
    res = bfs(tomato, green)
    print(res)