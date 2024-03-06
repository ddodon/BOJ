# not in 대신 v배열로 구름 유무 검사 (시간 줄이기 실험)

# 8방향
di = [0,-1,-1,-1,0,1,1,1]
dj = [-1,-1,0,1,1,1,0,-1]

# 대각방향
xi = [-1,-1,1,1]
xj = [-1,1,1,-1]

def move(lst,d,s):
    d = d-1
    c_move = []
    for ci,cj in lst:
        ni = (ci+di[d]*s)%(N)
        nj = (cj+dj[d]*s)%(N)
        arr[ni][nj]+=1 #비
        c_move.append((ni,nj))
    return c_move

def rain(lst): #구름 위치에 물 복사
    for ci,cj in lst:
        cnt = 0
        for x in range(len(xi)):
            ni = ci + xi[x]
            nj = cj + xj[x]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] > 0:
                cnt += 1
        arr[ci][cj] += cnt


N,M= map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

clouds = [(N-2,0),(N-2,1),(N-1,0),(N-1,1)]
for _ in range(M):
    # d:방향, s: 거리
    d, s = map(int,input().split())
    n_clouds = move(clouds,d,s) #이동 후 구름 위치
    rain(n_clouds) #물복사
    clouds = []

    v = [[False] * N for _ in range(N)]
    for ci, cj in n_clouds:
        v[ci][cj] = True

    for i in range(N):
        for j in range(N):
            if arr[i][j]<2: continue
            if v[i][j]: continue
            arr[i][j] -= 2
            clouds.append((i,j))
ans = 0
for i in range(N):
    for j in range(N):
        ans += arr[i][j]
print(ans)