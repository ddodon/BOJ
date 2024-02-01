# 8방향
di = [-2, -1, 1, 2, 2, 1, -1, -2]
dj = [1, 2, 2, 1, -1, -2, -2, -1]


# 최소거리 탐색 BFS
def bfs(si, sj, ei, ej):
    q = []
    v = [[0] * l for _ in range(l)]  # 방문체크
    ans = []  # 순서 확인 디버그용

    q.append([si, sj])
    v[si][sj] = 1
    ans.append([si, sj])

    while q:
        c = q.pop(0)
        if ei == c[0] and ej == c[1]:
            return v[c[0]][c[1]] - 1
        for k in range(len(di)):
            ni = c[0] + di[k]
            nj = c[1] + dj[k]
            if 0 <= ni < l and 0 <= nj < l and v[ni][nj] == 0:  # 범위 내 + 미방문지역
                v[ni][nj] = v[c[0]][c[1]] + 1
                ans.append([ni, nj])
                q.append([ni, nj])
    return -1  # 이동불가


TC = int(input())
for i in range(TC):
    l = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    res = bfs(si, sj, ei, ej)
    print(res)