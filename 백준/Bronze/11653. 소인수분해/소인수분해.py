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
n = int(input())
if n == 1:
    print()
elif prime(n) == 1:
    print(n)
else:
    d = 2
    while n != 1:
        if n % d == 0:
            n /= d
            print(d)
        else:
            d += 1