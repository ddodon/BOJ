di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]


def fish_move(arr, num):
    for i in range(4):
        for j in range(4):
            if arr[i][j] and arr[i][j][0] == num:
                fish, d = arr[i][j]
                for k in range(len(di)):
                    nd = (d + k) % 8
                    ni = i + di[nd]
                    nj = j + dj[nd]
                    if 0 <= ni < 4 and 0 <= nj < 4 and (arr[ni][nj][0] == 0 or arr[ni][nj][0] != -1):
                        arr[i][j] = [fish, nd]
                        arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
                        return arr
    return arr

def play(arr):
    for num in range(1, 17):
        arr = fish_move(arr, num)
    return arr

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
            dfs(n+1,sm,play(arr))
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
arr = play(arr)
dfs(0,ate_fish,arr)
print(ans)