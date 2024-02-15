from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(si, sj, v, s, ans):
    global cnt
    if arr[si][sj] != s or v[si][sj] == 1:
        return 0
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] == s:
                q.append((ni, nj))
                v[ni][nj] = 1
                cnt += 1
    ans = cnt ** 2
    return ans


M, N = map(int, input().split())
arr = [list(input()) for _ in range(N)]
V_W = [[0] * M for _ in range(N)]
V_B = [[0] * M for _ in range(N)]
ans_w = ans_b = 0
cnt = 0
tmp = 0
for i in range(N):
    for j in range(M):
        ans_w += bfs(i, j, V_W, 'W', ans_w)
        ans_b += bfs(i, j, V_B, 'B', ans_b)
print(ans_w)
print(ans_b)