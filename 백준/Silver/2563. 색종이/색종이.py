arr = [[0]*100 for _ in range(100)]
n = int(input())

for _ in range(n):
    a, b = map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            arr[i][j] = 1

tot = 0
for i in range(100):
    tot += arr[i].count(1)
print(tot)
#리스트 초기화 할 때 주의