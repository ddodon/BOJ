# 시계 8방향
di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]

# 볼 이동
def move(ci,cj,size):
    for _ in range(size):
        m,s,d = arr[ci][cj].pop(0)
        ni = (ci+s*di[d])%N
        nj = (cj+s*dj[d])%N
        arr[ni][nj].append((m,s,d))

def change(ci,cj):
    size = len(arr[ci][cj])
    tmp_d = [] # 방향 모아둘 배열
    sm_m = 0 # 질량 합
    sm_s = 0 # 속력 합
    dir = []
    for m,s,d in (arr[ci][cj]): # 파이어볼 합치기
        tmp_d.append(0 if d%2==0 else 1) # 방향이 짝수면 0저장
        sm_m += m
        sm_s += s

    if sum(tmp_d) == 0 or sum(tmp_d) == size:
        dir = [0,2,4,6]
    else:
        dir = [1,3,5,7]

    arr[ci][cj] = []

    for i in range(4):
        # 질량이 0인 파이어볼 소멸
        if sm_m//5 < 1:
            continue
        arr[ci][cj].append((sm_m//5,sm_s//size,dir[i]))

# 0. 입력
N,M,K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]
ans = 0
for _ in range(M):
    # 행 / 열 / m질량 / s속력 / d방향
    r,c,m,s,d = map(int,input().split())
    (r,c) = (r-1,c-1) # 좌표 맞추기
    arr[r][c].append((m,s,d))

# 명령 K번 반복
for t in range(K):
    ball = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                ball.append((i,j,len(arr[i][j])))

    # 1. 이동
    for i,j,size in ball:
        move(i,j,size)

    # 2. 2칸 파이어볼 검사
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) >= 2:
                change(i,j)

# 3. 남은 파이어볼 질량 합 계산
for i in range(N):
    for j in range(N):
            if arr[i][j]:
                for tm,ts,td in arr[i][j]:
                    ans += tm
print(ans)