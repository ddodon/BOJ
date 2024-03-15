di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def dfs(n,dir):
    global mn
    if n == K:
        v = [[1] * M for _ in range(N)]
        mn = min(mn,check(dir,v))
        return
    for d in range(4):
        dfs(n + 1, dir + [d])

def check(dir,v):
    for i in range(K):
        (ci,cj)=cctv[i]
        if arr[ci][cj] == 1: v = cctv_1(ci,cj,dir[i],v)
        elif arr[ci][cj] == 2: v = cctv_2(ci,cj,dir[i],v)
        elif arr[ci][cj] == 3: v = cctv_3(ci, cj, dir[i], v)
        elif arr[ci][cj] == 4: v = cctv_4(ci,cj,dir[i],v)
        elif arr[ci][cj] == 5: v = cctv_5(ci, cj, dir[i], v)
    return sum(map(sum,v))

def cctv_1(ci,cj,d,v):
    v[ci][cj] = 0
    while 1:
        ni = ci+di[d]
        nj = cj+dj[d]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]!=6:
            v[ni][nj]=0
            ci,cj = ni,nj
        else: break
    return v

def cctv_2(si,sj,d,v):
    ci, cj = si, sj
    v[ci][cj] = 0
    for t in range(0,3,2):
        ci, cj = si, sj
        while 1:
            ni = ci+di[(d+t)%4]
            nj = cj+dj[(d+t)%4]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]!=6:
                v[ni][nj]=0
                ci,cj = ni,nj
            else: break
    return v

def cctv_3(si,sj,d,v):
    ci, cj = si, sj
    v[ci][cj] = 0
    for t in range(2):
        ci, cj = si, sj
        while 1:
            ni = ci+di[(d+t)%4]
            nj = cj+dj[(d+t)%4]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]!=6:
                v[ni][nj]=0
                ci,cj = ni,nj
            else: break
    return v

def cctv_4(si,sj,d,v):
    ci, cj = si, sj
    v[ci][cj] = 0
    for t in range(3):
        ci, cj = si, sj
        while 1:
            ni = ci+di[(d+t)%4]
            nj = cj+dj[(d+t)%4]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]!=6:
                v[ni][nj]=0
                ci,cj = ni,nj
            else: break
    return v

def cctv_5(si,sj,d,v):
    ci, cj = si, sj
    v[ci][cj] = 0
    for t in range(4):
        ci, cj = si, sj
        while 1:
            ni = ci+di[t]
            nj = cj+dj[t]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]!=6:
                v[ni][nj]=0
                ci,cj = ni,nj
            else: break
    return v



N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cctv = []
wall = 0
for i in range(N):
    for j in range(M):
        if 1<=arr[i][j]<=5:
            cctv.append((i,j))
        elif arr[i][j] == 6:
            wall+=1
K = len(cctv)
mn = 21e8
dfs(0,[])
print(mn-wall)