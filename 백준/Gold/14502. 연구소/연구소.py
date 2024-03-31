from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(arr, lst):
    for num in lst:
        bi,bj = blank[num]
        arr[bi][bj]=1
    q = deque()
    death = 0
    for vi, vj in virus:
        q.append((vi, vj))
    while q:
        ci, cj = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                arr[ni][nj]=2
                death+=1
                q.append((ni,nj))

    return len(blank)-death-len(lst)

def dfs(n, idx, tlst):
    global ans
    if n == 3:
        trr = [lst[:] for lst in arr]
        res = bfs(trr, tlst)
        ans = max(res, ans)
        return

    for j in range(idx, len(blank)):
        if v[j] == 0:
            v[j] = 1
            dfs(n + 1, j + 1, tlst + [j])
            v[j] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
blank = []
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            blank.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))
v = [0] * (len(blank))
ans = 0  # 최대 안전영역

# dfs로 벽을 세울 수 있는 조합 구하기
dfs(0, 0, [])
print(ans)