from collections import deque
def bfs(si, sj, ei, ej):
    q = deque()
    v = [0] * (N + 1)  # 시작+편의점+락페 도착여부체크
    q.append([si, sj])  # 시작좌표
    v[0] = 1
    while q:
        ci, cj = q.popleft()
        if abs(ei - ci) + abs(ej - cj) <= 1000:
            return "happy"
        for i in range(len(conv)):
            a = abs(ci - conv[i][0]) + abs(cj - conv[i][1])
            if a <= 1000 and v[i + 1] == 0:
                v[i + 1] = 1
                q.append((conv[i][0], conv[i][1]))
    return "sad"


TC = int(input())
for _ in range(TC):
    N = int(input())  # 편의점의 개수
    Sj, Si = map(int, input().split())  # (x,y) 좌표 -> (j,i)
    conv = [list(map(int, input().split())) for _ in range(N)]
    Ej, Ei = map(int, input().split())
    for lst in conv:
        lst[0], lst[1] = lst[1], lst[0]  # 편의점 좌표 갱신

    res = bfs(Si, Sj, Ei, Ej)
    print(res)