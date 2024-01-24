# 방향: 상 하 좌 우
di = [-1,1,0,0]
dj = [0,0,-1,1]
# 1) 가로 세로 100인 도화지 + 0으로 둘러싸기
arr = [[0]*101 for _ in range(101)]
n = int(input())
# 2) 색종이 붙이기 (자연수만 들어옴)
for _ in range(n):
    a, b = map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            arr[i][j] = 1
res = 0
for i in range(1,101):
    for j in range(1,101):
        tmp = 0
        for k in range(4):
            if i+di[k] < 1 or j+dj[k] < 1 or i+di[k] >= 101 or j+dj[k] >= 101:
                continue
            else:
                if arr[i][j] == 1:
                    tmp += arr[i+di[k]][j+dj[k]]
        if tmp in (1,3):
            res += 1
        if tmp == 2:
            res += 2
print(res)