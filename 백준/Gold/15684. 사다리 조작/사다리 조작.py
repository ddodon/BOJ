def check(v):
    for j in range(N):
        start = j
        end = j
        for i in range(H + 1):
            if v[i][end] == 1:
                end -= 1
            elif v[i][end + 1] == 1:
                end += 1
        if start != end:
            return 0
    return 1


def dfs(n, idx, v):
    global ans
    # 가지치기
    if ans <= n:
        return
    if n > 3:
        return
    if check(v):
        ans = min(n, ans)
        return
    for j in range(idx, len(can_make_pos)):
        li, lj = can_make_pos[j]
        if v[li][lj] == 0 and v[li][lj - 1] == 0 and v[li][lj + 1] == 0:
            v[li][lj] = 1
            dfs(n + 1, j, v)
            v[li][lj] = 0


N, M, H = map(int, input().split())
v = [[0] * (N + 2) for _ in range(H + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    v[a][b] = 1
can_make_pos = []  # 사다리 설치 가능 위치
for i in range(1, H + 1):
    for j in range(1, N + 1):
        if v[i][j] == 0 and v[i][j - 1] == 0 and v[i][j + 1] == 0:
            can_make_pos.append((i, j))
ans = 21e8
dfs(0, 0, v)
print(-1 if ans == 21e8 else ans)