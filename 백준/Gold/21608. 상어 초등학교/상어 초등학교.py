from collections import defaultdict

di = [-1,0,1,0]
dj = [0,1,0,-1]

def seat(a,b,c,d):
    loc = []
    # 선호 학생 수/빈칸/좌표
    for i in range(N):
        for j in range(N):
            blank = 0
            like = 0
            if arr[i][j] != 0: continue
            for k in range(len(di)):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj] == 0:
                        blank += 1
                    elif arr[ni][nj] in (a,b,c,d):
                        like += 1
            loc.append((like,blank,i,j))
    return loc



N = int(input())
arr = [[0] * N for _ in range(N)]
dic = defaultdict(int)
s,a,b,c,d = map(int, input().split())
dic[s] = (a, b, c, d)
arr[1][1] = s # 첫번째 학생 자리는 고정


for i in range(1, N**2): # 두번째 학생부터
    s, a, b, c, d = map(int, input().split())
    dic[s] = (a, b, c, d)
    new_seat = seat(a,b,c,d)
    new_seat.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    arr[new_seat[0][2]][new_seat[0][3]]=s

ans = 0

for i in range(N):
    for j in range(N):
        like = 0
        for k in range(len(di)):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] in dic[arr[i][j]]:
                    like += 1
        if like == 1:
            ans += 1
        elif like == 2:
            ans += 10
        elif like == 3:
            ans += 100
        elif like == 4:
            ans += 1000
print(ans)