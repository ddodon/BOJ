from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def dfs(n, idx, tlst):
    global ans
    # M개 바이러스 선택
    if n == M:
        res = spread(tlst)
        ans = min(ans, res)
        return

    for j in range(idx, len(virus)):
        if virus_v[j] == 0:
            virus_v[j] = 1
            dfs(n + 1, j, tlst + virus[j])
            virus_v[j] = 0


def spread(active_viruses):
    q = deque()
    v = [[0] * N for _ in range(N)]
    for vi, vj in active_viruses:
        q.append((vi, vj))
        v[vi][vj] = 1
    cnt = 0
    while q:
        ci, cj = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]!=1:
                # 비활성 바이러스
                if arr[ni][nj]==2:
                    v[ni][nj] = v[ci][cj]+1
                else:
                    v[ni][nj] = v[ci][cj]+1
                    cnt += 1
                    if blank == cnt:
                        return (max(map(max, v))) - 1
                q.append((ni,nj))


    else:
        return 21e8

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
blank = 0 #남은 빈칸 개수
ans = 21e8
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append([(i, j)])
        elif arr[i][j] == 0:
            blank += 1
virus_v = [0] * len(virus)
dfs(0, 0, [])
if blank == 0:
    print(0)
else:
    print(-1 if ans==21e8 else ans)