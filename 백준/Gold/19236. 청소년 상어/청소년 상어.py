# 총 시간: 
# 문제 읽기
# 풀이 구상: 
# 로직 구현: 
# 오류 수정: 
# 제출 결과: 제한 시간 초과(/)
# 오류 부분: 물고기 이동 시 방향 미적용
from collections import defaultdict

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]


def move_fish(arr):
    dic = defaultdict(list)  # 방향 / 행 / 열
    nrr = [[l[:] for l in lst] for lst in arr]
    for i in range(N):
        for j in range(N):
            if arr[i][j][0] > 0:
                dic[arr[i][j][0]] = [arr[i][j][1], i, j]
    fish = sorted((k for k in dic.keys()))
    for fish_num in fish:
        dir, ci, cj = dic[fish_num]
        cnt = 0
        while cnt < 8:
            ni = ci + di[dir]
            nj = cj + dj[dir]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj][0] != -1:
                n_fish_num, n_dir = nrr[ni][nj]
                nrr[ci][cj][1] = dir
                nrr[ci][cj], nrr[ni][nj] = nrr[ni][nj], nrr[ci][cj]
                dic[fish_num] = [dir, ni, nj]
                dic[n_fish_num] = [n_dir, ci, cj]
                break
            else:
                dir = (dir + 1) % 8
                cnt += 1
    return nrr


def dfs(n, sm, arr):
    global ans
    can_eat,si,sj = eat(arr)
    if not can_eat:
        ans = max(ans,sm)
        return
    else:
        tmp_arr = [[l[:] for l in lst] for lst in arr]
        for j in range(len(can_eat)):
            ci,cj = can_eat[j]
            arr[si][sj][0] = 0
            sm += arr[ci][cj][0]
            arr[ci][cj][0] = -1
            dfs(n+1,sm,move_fish(arr))
            arr = [[l[:] for l in lst] for lst in tmp_arr]
            can_eat, si, sj = eat(arr)
            ci, cj = can_eat[j]
            sm -= arr[ci][cj][0]

def eat(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j][0] == -1:
                shark = [i, j, arr[i][j][0], arr[i][j][1]]
                break
    can_eat = []
    si, sj, s, sd = shark
    for k in range(1, N):
        ni = si + (di[sd] * k)
        nj = sj + (dj[sd] * k)
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj][0] > 0:
            can_eat.append((ni, nj))
    return (can_eat,si,sj)

N = 4
arr = [[[] for _ in range(N)] for _ in range(N)]
for t in range(N):
    tmp = list(map(int, input().split()))
    for i in range(0, len(tmp), 2):
        arr[t][i // 2] = [tmp[i], tmp[i + 1] - 1]

ans = 0
ate_fish = arr[0][0][0]
arr[0][0][0] = -1  # dead
arr = move_fish(arr)
dfs(0,ate_fish,arr)
print(ans)