from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj):
    q = deque()
    v = [[0] * M for _ in range(N)]
    sv = [[0] * M for _ in range(N)]
    q.append((si, sj))
    v[si][sj] = 1
    super_q = deque()
    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (pi, pj):
            super_q.append((pi, pj))
            sv[pi][pj] = v[ci][cj]
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if (arr[ni][nj] == 0 or arr[ni][nj] == 2) and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1

    while super_q:
        sci, scj = super_q.popleft()
        for k in range(len(di)):
            sni = sci + di[k]
            snj = scj + dj[k]
            if not (0 <= sni < N and 0 <= snj < M): continue
            if (sv[sni][snj] == 0):
                super_q.append((sni, snj))
                sv[sni][snj] = sv[sci][scj] + 1

    if v[ei][ej] and sv[ei][ej]:
        return min(v[ei][ej] - 1, sv[ei][ej] - 1)
    elif sv[ei][ej]:
        return sv[ei][ej] - 1
    elif v[ei][ej]:
        return v[ei][ej] - 1
    else:
        return min(v[ei][ej] - 1, sv[ei][ej] - 1)


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            pi, pj = i, j
            break
si, sj, ei, ej = 0, 0, N - 1, M - 1
ans = bfs(si, sj)
print("Fail" if (ans > T or ans == -1) else ans)