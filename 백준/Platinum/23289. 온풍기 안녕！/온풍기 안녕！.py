from collections import deque

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
dir = [(-1, 1), (0, 1), (1, 1)]
xdi = [-1, 0, 1]
xdj = [1, 1, 1]
opp = {}


def bfs(si, sj, d):
    q = deque()
    q.append((si, sj))
    v = [[0]*C for _ in range(R)]
    v[si][sj] = 5
    while q:
        ci, cj = q.popleft()
        if v[ci][cj] == 0:
            break
        for k in range(3):
            if d == 0:
                ni = ci + xdi[k]
                nj = cj + xdj[k]
                if 0 <= ni < R and 0 <= nj < C and v[ni][nj] == 0:
                    if k == 0:  # 대각선 위
                        if ((ci, cj), (ni, cj)) in walls or ((ni, cj), (ni, nj)) in walls: continue
                    elif k == 1:  # 직선
                        if ((ci, cj), (ni, nj)) in walls: continue
                    else:  # 대각선 아래
                        if ((ci, cj), (ni, cj)) in walls or ((ni, cj), (ni, nj)) in walls: continue
                    v[ni][nj] = v[ci][cj] - 1
                    q.append((ni, nj))

            elif d == 1:
                ni = ci + xdi[k]
                nj = cj - xdj[k]
                if 0 <= ni < R and 0 <= nj < C and v[ni][nj] == 0:
                    if k == 0:  # 대각선 위
                        if ((ci, cj), (ni, cj)) in walls or ((ni, cj), (ni, nj)) in walls: continue
                    elif k == 1:  # 직선
                        if ((ci, cj), (ni, nj)) in walls: continue
                    else:  # 대각선 아래
                        if ((ci, cj), (ni, cj)) in walls or ((ni, cj), (ni, nj)) in walls: continue
                    v[ni][nj] = v[ci][cj] - 1
                    q.append((ni, nj))
            elif d == 2:
                ni = ci - xdj[k]
                nj = cj + xdi[k]
                if 0 <= ni < R and 0 <= nj < C and v[ni][nj] == 0:
                    if k == 0:  # 대각선 위
                        if ((ci, cj), (ci, nj)) in walls or ((ci, nj), (ni, nj)) in walls: continue
                    elif k == 1:  # 직선
                        if ((ci, cj), (ni, nj)) in walls: continue
                    else:  # 대각선 아래
                        if ((ci, cj), (ci, nj)) in walls or ((ci, nj), (ni, nj)) in walls: continue
                    v[ni][nj] = v[ci][cj] - 1
                    q.append((ni, nj))
            else:
                ni = ci + xdj[k]
                nj = cj - xdi[k]
                if 0 <= ni < R and 0 <= nj < C and v[ni][nj] == 0:
                    if k == 0:  # 대각선 위
                        if ((ci, cj), (ci, nj)) in walls or ((ci, nj), (ni, nj)) in walls: continue
                    elif k == 1:  # 직선
                        if ((ci, cj), (ni, nj)) in walls: continue
                    else:  # 대각선 아래
                        if ((ci, cj), (ci, nj)) in walls or ((ci, nj), (ni, nj)) in walls: continue
                    v[ni][nj] = v[ci][cj] - 1
                    q.append((ni, nj))
    return v


def heating(temp):
    for d, ci, cj in heater:
        ci = ci + di[d - 1]
        cj = cj + dj[d - 1]
        res = bfs(ci, cj, d - 1)
        for i in range(R):
            for j in range(C):
                temp[i][j]+=res[i][j]
    return temp

def adjust(arr):
    nrr = [lst[::] for lst in arr]
    for i in range(R):
        for j in range(C):
            if arr[i][j]>0:
                ci,cj=i,j
                for k in range(len(di)):
                    ni = ci+di[k]
                    nj = cj+dj[k]
                    if 0<=ni<R and 0<=nj<C and arr[ci][cj]>arr[ni][nj]:
                        if ((ci,cj),(ni,nj)) in walls: continue
                        diff = (arr[ci][cj]-arr[ni][nj])//4
                        nrr[ci][cj] -= diff
                        nrr[ni][nj] += diff
    return nrr

def side(arr):
    for i in range(R):
        if arr[i][0]>0:
            arr[i][0]-=1
        if arr[i][C-1]>0:
            arr[i][C-1]-=1

    for j in range(1,C-1):
        if arr[0][j]>0:
            arr[0][j]-=1
        if arr[-1][j]>0:
            arr[-1][j]-=1
    return arr

def check():
    for ci,cj in to_check:
        if temp[ci][cj]<K:
            return False
    return True




R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
temp = [[0] * C for _ in range(R)]
to_check = []  # 조사칸
heater = []  # 온풍기
for i in range(R):
    for j in range(C):
        if arr[i][j] == 5:
            to_check.append((i, j))
        elif 0 < arr[i][j] < 5:
            heater.append((arr[i][j], i, j))
W = int(input())
walls = set()
for _ in range(W):
    x, y, t = map(int, input().split())
    x, y = x - 1, y - 1
    if t == 0:
        walls.add(((x, y), (x - 1, y)))
        walls.add(((x - 1, y), (x, y)))
    else:
        walls.add(((x, y), (x, y + 1)))
        walls.add(((x, y + 1), (x, y)))

choco = 0

for _ in range(100):
    # 1. 온풍기에서 바람
    temp = heating(temp)

    # 2. 온도 조절
    temp = adjust(temp)

    # 3. 테두리 -1
    temp = side(temp)

    # 4. 초코 +1
    choco += 1

    # 5. 조사
    if check():
        print(choco)
        break
else:
    print(101)