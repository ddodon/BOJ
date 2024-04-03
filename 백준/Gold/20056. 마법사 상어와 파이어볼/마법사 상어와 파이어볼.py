# 디폴트딕트 활용한 구현
from collections import defaultdict

# 시계 8방향
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]


# 볼 이동
def move(fireballs):
    dic = defaultdict(list)
    for fireball in fireballs:
        ci, cj, cm, cs, cd = fireball
        ni = (ci + di[cd] * cs) % N
        nj = (cj + dj[cd] * cs) % N
        dic[(ni, nj)].append((cm, cs, cd))
    return dic


# 볼 변화
def change(balls_now):
    balls_changed = []  # 변화를 거친 파이어볼 리턴
    for k, v in balls_now.items():
        if len(v) >= 2:  # 파이어볼 2개 이상
            sm_m = 0  # 질량 합
            sm_s = 0  # 속력 합
            set_d = set()  # 방향 set
            for m, s, d in v:
                sm_m += m
                sm_s += s
                set_d.add(d % 2)
            if sm_m // 5:
                if len(set_d) == 1:
                    dir = [0, 2, 4, 6]
                else:
                    dir = [1, 3, 5, 7]
                for d in range(4):
                    i, j = k
                    balls_changed.append((i, j, sm_m // 5, sm_s // len(v), dir[d]))
            else:
                continue
        else:  # 파이어볼 하나
            i, j = k
            m, s, d = v[0]
            balls_changed.append((i, j, m, s, d))
    return balls_changed


# 입력
N, M, K = map(int, input().split())
fireball = []
ans = 0
for _ in range(M):
    # 행 / 열 / m질량 / s속력 / d방향
    r, c, m, s, d = map(int, input().split())
    (r, c) = (r - 1, c - 1)  # 좌표 맞추기
    fireball.append((r, c, m, s, d))

# 명령 K번 반복
for t in range(K):
    # 1. 이동 (딕셔너리에 파이어볼 모음 삽입)
    balls_now = move(fireball)
    # 2. 파이어볼의 변화
    fireball = change(balls_now)

for ball in fireball:
    ans += ball[2]
print(ans)