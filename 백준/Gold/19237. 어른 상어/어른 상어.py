from collections import defaultdict

di = [-1,1,0,0]
dj = [0,0,-1,1]


def smelling():
    for i in range(N):
        for j in range(N):
            if arr[i][j]>0:
                smell[i][j] = [K,arr[i][j]]
def dismelling():
    for i in range(N):
        for j in range(N):
            if smell[i][j] and smell[i][j][0]>0:
                smell[i][j][0] -= 1
                if smell[i][j][0]==0:
                    smell[i][j] = []

def move(arr):
    nrr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]>0:
                ci,cj = i,j
                blank = []
                same = []

                for k in range(len(di)):
                    ni = ci+di[k]
                    nj = cj+dj[k]
                    if 0<=ni<N and 0<=nj<N:
                        if smell[ni][nj]==[]:
                            blank.append([k+1,(ni,nj)])
                        elif smell[ni][nj] and smell[ni][nj][1] == arr[i][j]:
                            same.append([k+1,(ni,nj)])
                sd = shark_dir[arr[ci][cj]] # 현재 상어가 보고 있는 방향
                pd = priority_dir[arr[ci][cj]] # 현재 상어의 방향 우선순위
                # 1) 인접한 칸 중 아무 냄새가 없는 칸
                if blank:
                    flag = False
                    for d in pd[sd-1]:
                        if flag == True: break
                        for nd,(nsi,nsj) in blank:
                            if d == nd:
                                if nrr[nsi][nsj]==0 or nrr[nsi][nsj]>arr[i][j]: # 상어가 없거나 지금 움직이는 상어가 더 강한 상어면
                                    nrr[nsi][nsj] = arr[i][j]
                                    shark_dir[arr[i][j]] = nd
                                    flag = True
                                    break
                                else:
                                    flag = True
                                    break
                # 2) 인접한 칸 중 자신의 냄새가 있는 칸
                else:
                    flag = False
                    for d in pd[sd-1]:
                        if flag == True: break
                        for nd,(nsi,nsj) in same:
                            if d == nd:
                                if nrr[nsi][nsj]==0 or nrr[nsi][nsj]>arr[i][j]: # 상어가 없거나 지금 움직이는 상어가 더 강한 상어면
                                    nrr[nsi][nsj] = arr[i][j]
                                    shark_dir[arr[i][j]] = nd
                                    flag = True
                                    break
                                else:
                                    flag = True
                                    break

    return nrr

N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
shark_dir = defaultdict(int) # 상어 초기 방향
tmp = list(map(int,input().split()))
for i in range(1,M+1):
    shark_dir[i] = tmp[i-1]
smell = [[[] for _ in range(N)] for _ in range(N)] # 상어 냄새
priority_dir = [[] for _ in range(M+1)] # 상어 이동 우선순위
for i in range(1,M+1):
    for _ in range(4):
        priority_dir[i].append(list(map(int,input().split())))
# 1. 자신의 자리에 냄새
smelling()
for time in range(1000):
    # 2. 상어 이동
    arr = move(arr)
    # 3. 냄새 -1
    dismelling()
    # 1. 자신의 자리에 냄새
    smelling()

    # 4. 상어 1마리 남았다면 break
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]>0:
                cnt+=1
    if cnt == 1:
        print(time+1)
        break
else:
    print(-1)