# 총 시간: 84분
# 문제 읽기: 14:01 ~ 14:17 (먼저 읽은 문제)
# 풀이 구상: 15:15 ~ 15:30
# 로직 구현: 15:30 ~ 16:00
# 오류 수정: 16:00 ~ 16:53
# 제출 결과: (1/2)
# 오류 부분: k칸 회전 빼먹음, '(i + di)%4' <- 배열 크기마다 달라져야 하는데 일반화 안함, zero division

di = [-1,0,1,0]
dj = [0,1,0,-1]

def rotate(lst,d,k):                            # 배열 회전
    dir = 1 if d==0 else -1
    new_lst = [0]*len(lst)
    for i in range(len(lst)):
        new_lst[i] = lst[(i-dir*k)%len(lst)]
    return new_lst

def check(i,j):                                 # 인접한 동일 숫자 삭제
    for k in range(len(di)):
        ni = i + di[k]
        nj = (j + dj[k])%(len(arr[0]))
        if 0<=ni<N and arr[i][j] == arr[ni][nj] and arr[i][j]!=0:
            same.append((ni,nj))
            same.append((i,j))


N,M,T = map(int,input().split())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i]=list(map(int,input().split()))

for t in range(T):
    x,d,k = map(int,input().split())
    for i in range(1,N+1):
        if i%x==0:
            arr[i-1] = rotate(arr[i-1],d,k)
    nzero=0
    for r in range(N):
        for c in range(len(arr[0])):
            if arr[r][c]>0:
                nzero+=1
    if not nzero: break
    avg = sum(map(sum,arr)) / nzero              # 평균
    same = []                                    # 같은 수 찾기
    for i in range(N):
        for j in range(len(arr[0])):
            check(i,j)
    if same:                                     # 같은 수가 있으면 삭제
        for (si,sj) in same:
            arr[si][sj] = 0
    else:                                        # 없으면 평균기준 연산
        for r in range(N):
            for c in range(len(arr[0])):
                if arr[r][c] > avg and arr[r][c]!=0:
                    arr[r][c] -= 1
                elif arr[r][c] < avg and arr[r][c]!=0:
                    arr[r][c] += 1
print(sum(map(sum,arr)))