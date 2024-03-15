from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def dfs(n, idx, tlst): # M개의 활성 바이러스 조합
    global ans
    if n == M:
        ans = min(ans, bfs(tlst))
        return

    for j in range(idx, len(virus)):
        if v[j] == 0:
            v[j] = 1
            dfs(n + 1, j+1, tlst + [virus[j]])
            v[j] = 0

def bfs(act): # 조합별 최소 시간 구하기
    q = deque()
    bfs_v = [[0] * N for _ in range(N)]
    for (ai, aj) in act:
        bfs_v[ai][aj] = 1
        q.append((ai, aj, 1))
    remain = blank
    while q:
        ci, cj, dist = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and bfs_v[ni][nj] == 0 and arr[ni][nj] != 1:
                if arr[ni][nj] == 0:
                    remain -= 1
                    bfs_v[ni][nj] = dist + 1
                    q.append((ni, nj, dist + 1))
                    if remain == 0:
                        return (max(map(max, bfs_v)) - 1)
                elif arr[ni][nj] == 2:
                    bfs_v[ni][nj] = dist
                    q.append((ni, nj, dist + 1))
    return 21e8


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 21e8
blank = 0

virus = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            blank += 1
        elif arr[i][j] == 2:
            virus.append((i, j)) # 빈칸과 바이러스의 좌표 담아두기
v = [0] * (len(virus) + 1)
if blank == 0:
    print(0)
    exit()
dfs(0, 0, [])
print(-1 if ans == 21e8 else ans)