n = int(input())
A = set(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

for i in range(m):
    if check[i] in A:
        print(1)
    else:
        print(0)