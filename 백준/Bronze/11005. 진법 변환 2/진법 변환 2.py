lst = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
n, b = map(int,input().split())
res = []

while n:
    res.append(lst[n%b])
    n = n // b
res=res[::-1]
print("".join(res))