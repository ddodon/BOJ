from collections import defaultdict, deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs():
    q = deque()
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                q.append((i, j))
    n_dust = defaultdict(int)
    while q:
        ci, cj = q.popleft()
        cnt = 0
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0<=ni<R and 0<=nj<C and arr[ni][nj]!= -1:
                cnt += 1
                n_dust[(ni,nj)] += arr[ci][cj]//5
        arr[ci][cj] -= (arr[ci][cj]//5*cnt)
    for (i,j),w in n_dust.items():
        arr[i][j] += w

def wind_up(air):
    u = air[0][0]
    up = deque()
    for i in range(1,C):
        up.append(arr[u][i])
    for i in range(u-1,0,-1):
        up.append((arr[i][C-1]))
    for i in range(C-1,-1,-1):
        up.append((arr[0][i]))
    for i in range(1,u):
        up.append((arr[i][0]))
    up.appendleft(0)
    up.pop()
    for i in range(1,C):
        arr[u][i] = up.popleft()
    for i in range(u-1,0,-1):
        arr[i][C-1] = up.popleft()
    for i in range(C-1,-1,-1):
        arr[0][i] = up.popleft()
    for i in range(1,u):
        arr[i][0] = up.popleft()


def wind_down(air):
    d = air[1][0]
    down = deque()
    for i in range(1,C):
        down.append(arr[d][i])
    for i in range(d+1,R-1):
        down.append(arr[i][C-1])
    for i in range(C-1,-1,-1):
        down.append(arr[R-1][i])
    for i in range(R - 2, d, -1):
        down.append(arr[i][0])
    down.appendleft(0)
    down.pop()
    for i in range(1,C):
        arr[d][i] = down.popleft()
    for i in range(d+1,R-1):
        arr[i][C-1] = down.popleft()
    for i in range(C-1,-1,-1):
        arr[R-1][i] = down.popleft()
    for i in range(R - 2, d, -1):
        arr[i][0] = down.popleft()


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
air = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            air.append((i, j))

for i in range(T):
    bfs()
    wind_up(air)
    wind_down(air)
print(sum(map(sum,arr))+2)