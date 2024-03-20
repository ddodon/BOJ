# 총 시간: 분
# 문제 읽기: 30분 ㄷㄷ
# 풀이 구상: 분
#   - 벽의 존재를 어떻게 구현할 것인가 고민 (멤버십 연산은 시간초과 우려) (2개 조합 최대 800개 연산을 매번)
#   - 벽만 표시해둔 V배열?
#   - 바람 전달 (BFS) -> 벽 만났을 때 방향별 처리 막힘
#   - 녹화시간 2시간 47분: 벽배열로 벽 판단 시 로직상 오류  (벽이 한 칸 떨어져 존재하는 경우 3칸 중 2칸은 벽이 없는데 있다고 판단)
#   - 벽을 set으로 두고 in 사용으로 전환
#   - type별로 ni nj 방향 다르게 설정하니 성공 (종료 10분전 ㅠ)
#   - 열 이동(move) 동시에 처리 -> 생각 안남 [배열 하나 더 만들어서] [빼줄 값, 더할 값 저장해두고] [합치기]
# 로직 구현: 분
# 제출 결과: 제한 시간 초과 (벽 처리에서 오래 걸림)
# 오류 부분:
# 오류 수정:
# 기타: 풀이시작 전 6분간 화장실

from collections import deque

# 방향 → ← ↑ ↓
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

# 바람 방향
hi = [[-1, 0, 1], [-1, 0, 1], [-1, -1, -1], [1, 1, 1]]
hj = [[1, 1, 1], [-1, -1, -1], [-1, 0, 1], [-1, 0, 1]]


def bfs(type, si, sj):
    heat = 5
    q = deque()
    q.append((si, sj, heat))
    v = [[0] * C for _ in range(R)]
    v[si][sj] = heat
    while q:
        ci, cj, ch = q.popleft()
        for k in range(len(hi[0])):
            ni = ci + hi[type - 1][k]
            nj = cj + hj[type - 1][k]
            if 0 <= ni < R and 0 <= nj < C and v[ni][nj] == 0:
                if ch - 1 > 0:
                    if type == 1 or type == 2:
                        if k == 0 and (((ci, cj), (ni, cj)) in wall or ((ni, cj), (ni, nj)) in wall): continue
                        if k == 1 and (((ci, cj), (ni, nj)) in wall): continue
                        if k == 2 and (((ci, cj), (ni, cj)) in wall or ((ni, cj), (ni, nj)) in wall): continue
                    elif type == 3 or type == 4:
                        if k == 0 and (((ci, cj), (ci, nj)) in wall or ((ci, nj), (ni, nj)) in wall): continue
                        if k == 1 and (((ci, cj), (ni, nj)) in wall): continue
                        if k == 2 and (((ci, cj), (ci, nj)) in wall or ((ci, nj), (ni, nj)) in wall): continue
                    v[ni][nj] = ch - 1
                    q.append((ni, nj, ch - 1))
    return v


def heating(home):
    for type, i, j in heater:
        si = i + di[type - 1]
        sj = j + dj[type - 1]
        tmp = bfs(type, si, sj)
        for r in range(R):
            for c in range(C):
                home[r][c] += tmp[r][c]
    return home


def move(home):
    new_home = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if home[i][j] != 0:
                ci, cj = i, j
                for k in range(len(di)):
                    ni = ci + di[k]
                    nj = cj + dj[k]
                    if 0 <= ni < R and 0 <= nj < C and (home[i][j] > home[ni][nj]):
                        if ((i, j), (ni, nj)) in wall: continue
                        new_home[i][j] -= (home[i][j] - home[ni][nj]) // 4
                        new_home[ni][nj] += (home[i][j] - home[ni][nj]) // 4
    for i in range(R):
        for j in range(C):
            home[i][j] += new_home[i][j]
    return home


def outline(home):
    for i in range(R):
        if home[i][0] > 0:
            home[i][0] -= 1
        if home[i][C - 1] > 0:
            home[i][C - 1] -= 1

    for i in range(1, C - 1):
        if home[0][i] > 0:
            home[0][i] -= 1
        if home[R - 1][i] > 0:
            home[R - 1][i] -= 1
    return home


R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
home = [[0] * C for _ in range(R)]  # 온도를 나타낼 배열 (home)
check = []  # 조사해야 하는 칸 (r,c)
heater = []  # 온풍기 좌표 (종류,r,c)
for i in range(R):
    for j in range(C):
        if arr[i][j] == 0: continue
        if arr[i][j] == 5:
            check.append((i, j))
        elif arr[i][j] < 5:
            heater.append((arr[i][j], i, j))
W = int(input())
wall = set()  # 벽이 있는 부분
for _ in range(W):
    x, y, t = map(int, input().split())
    x, y = x - 1, y - 1
    if t == 0:
        wall.add(((x, y), (x - 1, y)))
        wall.add(((x - 1, y), (x, y)))
    else:
        wall.add(((x, y), (x, y + 1)))
        wall.add(((x, y + 1), (x, y)))
choco = 0  # 초콜릿
while 1:
    if choco > 100: break
    home = heating(home)
    home = move(home)
    home = outline(home)
    choco += 1
    cnt = 0
    for ci, cj in check:
        if home[ci][cj] >= K:
            cnt += 1
    if cnt >= len(check):
        break
print(choco)