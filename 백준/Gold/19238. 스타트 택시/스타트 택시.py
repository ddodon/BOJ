from collections import deque, defaultdict

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    v = [[0] * N for _ in range(N)]
    v[si][sj] = 1
    customer = []
    while q:
        ci, cj = q.popleft()
        if passenger[ci][cj] > 0:
            customer.append((v[ci][cj] - 1, ci, cj, passenger[ci][cj]))
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
    if customer:
        customer.sort()
        return customer[0]
    return 0


def drive(si, sj, num):
    q = deque()
    q.append((si, sj))
    v = [[0] * N for _ in range(N)]
    v[si][sj] = 1
    (ei, ej) = depart[num]
    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (ei, ej):
            return (v[ci][cj] - 1, ci, cj)
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
    return 0


N, M, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
passenger = [[0] * N for _ in range(N)]
si, sj = map(int, input().split())
si, sj = si - 1, sj - 1
depart = defaultdict(tuple)
for m in range(1, M + 1):
    pi, pj, ei, ej = map(int, input().split())
    pi, pj, ei, ej = pi - 1, pj - 1, ei - 1, ej - 1
    passenger[pi][pj] = m
    depart[m] = (ei, ej)

for _ in range(M):
    # 1. 승객 고르기
    res = bfs(si, sj)
    # 1-1. 손님 태우러 못가는 경우
    if not res:
        print(-1)
        break
    dist, pi, pj, num = res
    # 1-2. 연료 감소, 연료 확인
    fuel -= dist
    if fuel < 0:
        print(-1)
        break
    si, sj = pi, pj
    passenger[pi][pj] = 0

    # 2. 손님 이송
    eres = drive(si, sj, num)
    if not eres:
        print(-1)
        break
    dist, ei, ej = eres
    # 연로 감소, 연료 확인
    fuel -= dist
    if fuel < 0:
        print(-1)
        break
    si, sj = ei, ej

    # 3. 연료 충전
    fuel += dist * 2
else:
    print(fuel)