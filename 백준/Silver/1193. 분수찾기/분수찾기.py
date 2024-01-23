x = int(input())
n = 1
a = 2
line = 1
while n < x:
    n += a
    a += 1
    line += 1
if line%2==0:
    print(line+x-n,"/",n-x+1,sep="")
else:
    print(n - x + 1, "/", line + x - n, sep="")