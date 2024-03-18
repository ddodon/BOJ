# 총 시간: 분
# 문제 읽기:  ~
# 풀이 구상:  ~
# 로직 구현:  ~ 2:07:00
# 오류 수정:  2:12:00 ~
# 제출 결과: (/3)
# 오류 부분: 정답 제출 위한 코드에서 방향 좌표 빼먹음 + 한줄 완성 시 터지고 움직일 때 처음부터 움직이게 설계함
# 1시간 30분 경 잠깐 휴식
# 틀렸습니다(1%)

di = [-1,0,1,0]
dj = [0,1,0,-1]

N = int(input())
A,B = 4,10

def to_blue(t,x,y):
    d = 1
    start = [(x,y)]
    if t==2: start.append((x,y+1))
    elif t==3: start.append((x+1,y))
    flag = True
    while flag:
        for n,(ci,cj) in enumerate(start):
            ni = ci+di[d]
            nj = cj+dj[d]
            if not(0<=ni<A and 0<=nj<B and blue[ni][nj]==0):
                flag = False
                num = n
                point=(ci,cj)
                break
            start[n] = (ni,nj)
    if num==0:
        for si,sj in start:
            blue[si][sj] = 1
    else:
        ei,ej = point
        if t==2:
            blue[ei][ej-1]=blue[ei][ej]=1
        else:
            blue[ei-1][ej]=blue[ei][ej] = 1
    return blue


def to_green(t,x,y):
    d = 2
    start = [(x,y)]
    if t==2: start.append((x,y+1))
    elif t==3: start.append((x+1,y))
    flag = True
    while flag:
        for n,(ci,cj) in enumerate(start):
            ni = ci+di[d]
            nj = cj+dj[d]
            if not(0<=ni<B and 0<=nj<A and green[ni][nj]==0):
                flag = False
                num = n
                point=(ci,cj)
                break
            start[n] = (ni,nj)
    if num==0:
        for si,sj in start:
            green[si][sj] = 1
    else:
        ei,ej = point
        if t==2:
            green[ei][ej-1]=green[ei][ej]=1
        else:
            green[ei-1][ej]=green[ei][ej] = 1
    return green


def check_green(arr):
    d = 2
    st = []
    cnt = 0 # 사라진 행의 수
    for i in range(B-1,A+1,-1):
        if arr[i].count(1)==4:
            cnt+=1
            arr[i] = [0]*A
            st.append(i)
    if st:
        for i in range(st[0],A-1,-1):
            for j in range(A-1,-1,-1):
                if arr[i][j]!=1: continue
                ci,cj = i, j
                for t in range(cnt):
                    ni,nj = ci+di[d],cj+dj[d]
                    if 0<=ni<B and arr[ni][nj]==0:
                        arr[ni][nj] = 1
                        arr[ci][cj] = 0
                        ci,cj = ni,nj
    return arr,cnt

def check_blue(arr):
    d = 2
    cnt = 0 # 사라진 열의 수
    st = []
    arr = [list(lst) for lst in zip(*arr[::-1])]
    for i in range(B-1,A+1,-1):
        if arr[i].count(1)==4:
            cnt+=1
            arr[i] = [0]*A
            st.append(i)
    if st:
        for i in range(st[0],A-1,-1):
            for j in range(A-1,-1,-1):
                if arr[i][j]!=1: continue
                ci,cj = i, j
                for t in range(cnt):
                    ni,nj = ci+di[d],cj+dj[d]
                    if 0<=ni<B and arr[ni][nj]==0:
                        arr[ni][nj] = 1
                        arr[ci][cj] = 0
                        ci,cj = ni,nj
    arr = [list(lst) for lst in zip(*arr)][::-1]
    return arr,cnt

def soft_blue(arr):
    d = 2
    cnt = 0
    arr = [list(lst) for lst in zip(*arr[::-1])]
    for i in range(A,A+2):
        if arr[i].count(1)>0:
            cnt+=1
    for j in range(cnt):
        arr[B-1-j] = [0]*A
    for i in range(B-1,A-1,-1):
        for j in range(A-1,-1,-1):
            if arr[i][j]!=1: continue
            ci,cj = i, j
            for t in range(cnt):
                ni,nj = ci+di[d],cj+dj[d]
                if 0<=ni<B and arr[ni][nj]==0:
                    arr[ni][nj] = 1
                    arr[ci][cj] = 0
                    ci,cj = ni,nj
    arr = [list(lst) for lst in zip(*arr)][::-1]
    return arr


def soft_green(arr):
    d = 2
    cnt = 0
    for i in range(A,A+2):
        if arr[i].count(1)>0:
            cnt+=1
    for j in range(cnt):
        arr[B-1-j] = [0]*A
    for i in range(B-1,A-1,-1):
        for j in range(A-1,-1,-1):
            if arr[i][j]!=1: continue
            ci,cj = i, j
            for t in range(cnt):
                ni,nj = ci+di[d],cj+dj[d]
                if 0<=ni<B and arr[ni][nj]==0:
                    arr[ni][nj] = 1
                    arr[ci][cj] = 0
                    ci,cj = ni,nj
    return arr


blue = [[0]*(B) for _ in range(A)]
green = [[0]*A for _ in range(B)]
ans = 0
for _ in range(N):
    t,x,y = map(int,input().split())
    blue = to_blue(t,x,y)
    green = to_green(t,x,y)

    green,g_cnt = check_green(green)
    ans += g_cnt
    blue,b_cnt = check_blue(blue)
    ans += b_cnt
    blue = soft_blue(blue)
    green = soft_green(green)
print(ans)
sm_blue = sum(map(sum,blue))
sm_green = sum(map(sum,green))
print(sm_blue+sm_green)