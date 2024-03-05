# 팀 나누기
def dfs(n, idx, tlst):
    if n == N // 2:
        team.append(tlst)
        return
    for j in range(idx, N):
        if v[n] == 0:
            v[n] = 1
            dfs(n + 1, j + 1, tlst + [j])
            v[n] = 0


# 능력치 계산
def ability(tlst):
    sm = 0
    for i in tlst:
        for j in tlst:
            if i != j:
                sm += arr[i][j]
    return sm


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [0] * N
team = []
dfs(0, 0, [])
team_s = team[:(len(team) // 2)]
team_l = team[(len(team) // 2):][::-1]

mn = 21e8
for s, l in zip(team_s, team_l):
    sm_s = ability(s)
    sm_l = ability(l)
    # print(s,sm_s,l,sm_l)
    mn = min(mn, abs(sm_s - sm_l))
print(mn)