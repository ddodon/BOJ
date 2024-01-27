n = int(input())
t = 2
cnt = 0
if n == 1:
    print(1)
else:
    while 1:
        if t >= n:
           break
        t *= 2
        cnt += 1
    print((n - (2 ** (cnt)))*2)