from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def find(bi, bj):
    q = deque()
    v = [[0] * N for _ in range(N)]
    q.append((bi, bj))
    v[bi][bj] = 1
    fishes = []
    while q:
        ci, cj = q.popleft()
        if fishes and v[ci][cj] > fishes[0][0]:
            fishes.sort()
            return fishes[0]
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] <= baby_shark_size:
                if 0 < arr[ni][nj] < baby_shark_size:
                    fishes.append((v[ci][cj], ni, nj))
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
    return 0


N = int(input())
# 9: 아기 상어, 0: 빈칸, 그 외: 물고기 크기
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            bi, bj = i, j
# 최초 아기 상어 크기: 2
baby_shark_size = 2

time = 0
ate_fish = 0  # 먹은 물고기 수
while 1:
    # 1. 먹을 물고기 없으면 엄마 부르기
    res = find(bi, bj)
    if not res:
        break

    # 2. 물고기 먹기
    t, fi, fj = res
    time += t
    arr[bi][bj] = 0
    arr[fi][fj] = 9
    bi, bj = fi, fj
    ate_fish += 1

    # 3. 먹은 물고기가 몸크기와 같으면 사이즈 +1
    if ate_fish == baby_shark_size:
        ate_fish = 0
        baby_shark_size += 1

print(time)