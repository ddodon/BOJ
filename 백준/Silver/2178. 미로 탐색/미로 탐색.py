# 방향: 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(s1, e1, s2, e2):  # 문제 -> (1,1) ~ (s2,e2)
    v = [[0] * (M) for _ in range(N)]
    q = []
    v[s1][e1] = 1
    q.append([s1, e1])

    while q:
        c = q.pop(0)  # -> List
        if [c[0], c[1]] == [s2, e2]:  # 도착지점
            return (v[c[0]][c[1]])
        for k in range(4):
            ni = c[0] + di[k]
            nj = c[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and maze[ni][nj] == 1:
                v[ni][nj] = v[c[0]][c[1]] + 1 #최단거리
                q.append([ni, nj])
    return 0


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
S = N - 1
E = M - 1

res = bfs(0, 0, S, E)
print(res)