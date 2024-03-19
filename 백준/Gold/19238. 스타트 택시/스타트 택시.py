# 총 시간: 분
# 문제 읽기: 5분
# 풀이 구상: 10분
# 로직 구현: ~3시 5분 (TC안맞음)
    # 8분: 손님까지의 거리와 손님번호 변수를 순서를 바꿔서 리턴했었음
# 제출 결과: (/2)
# 오류 부분: TypeError (?)
# 오류 수정: 손님을 태우고 목적지까지 갈 수 없는 경우 None 리턴했었음 (다 벽이거나)

from collections import deque, defaultdict

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj):
    # global - 남은 손님 수 (가지치기 용)
    q = deque()
    v = [[0] * N for _ in range(N)]
    q.append((si, sj))
    v[si][sj] = 1
    customers = []
    while q:
        ci, cj = q.popleft()
        if p_arr[ci][cj] != 0:
            customers.append((v[ci][cj] - 1, ci, cj, p_arr[ci][cj]))
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
    if customers:
        customers.sort()
        return customers[0]
    else:
        return 0


def drive(si, sj):
    q = deque()
    v = [[0] * N for _ in range(N)]
    q.append((si, sj))
    v[si][sj] = 1
    (ei, ej) = departure[pi, pj]
    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (ei, ej):
            return (ei, ej, v[ci][cj] - 1)
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
    return 0


N, M, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
p_arr = [[0] * N for _ in range(N)]
si, sj = map(int, input().split())
si, sj = si - 1, sj - 1
passengers = []
departure = defaultdict(tuple)
for i in range(1, M + 1):
    pi, pj, ei, ej = map(int, input().split())
    pi, pj, ei, ej = pi - 1, pj - 1, ei - 1, ej - 1
    p_arr[pi][pj] = i
    departure[(pi, pj)] = (ei, ej)

for _ in range(M):
    # 손님 고르기
    customer = bfs(si, sj)
    if not customer:
        print(-1)
        break

    p_dist, pi, pj, p_num = customer
    if fuel - p_dist < 0:
        print(-1)
        break
    fuel -= p_dist

    # 운전
    p_arr[pi][pj] = 0
    si, sj = pi, pj
    arrived = drive(si, sj)
    if not arrived:
        print(-1)
        break
    ei, ej, e_dist = arrived
    if fuel - e_dist < 0:
        print(-1)
        break
    fuel -= e_dist
    si, sj = ei, ej

    # 연료 충언
    fuel += (e_dist) * 2
else:
    print(fuel)