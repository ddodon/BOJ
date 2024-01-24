n = int(input())
if n > 1 and n<=10:
    arr = [[0]*101 for _ in range(101)]
else:
    arr = [[0]*1001 for _ in range(1001)]

for t in range(1,n+1): #n번 색종이 쌓기
    # (0,0)을 가장 왼쪽 위 칸으로 가정
    a,b,c,d = map(int,input().split())
    for i in range(d):
        for j in range(c):
            arr[a+j][b+i] = t
for t in range(1,n+1):
    sm = 0 #색종이 넓이
    for i in range(len(arr)):
        sm += (arr[i].count(t))
    print(sm)