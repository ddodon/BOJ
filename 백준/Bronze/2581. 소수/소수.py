def prime(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2,int(n**(0.5)+1)):
            if n % i == 0:
                return 0
        return 1

m = int(input())
n = int(input())
res = 0
res2 = n
for i in range(m,n+1):
    if prime(i) == 1:
        res += i
        if res2 > i:
            res2 = i
    else:
        continue
if res == 0:
    print(-1)
else:
    print(res)
    print(res2)