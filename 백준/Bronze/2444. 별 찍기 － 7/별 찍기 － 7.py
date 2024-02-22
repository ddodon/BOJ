n=int(input())
align = (2*n)-1
for i in range(1, n*2):
    if i <= n:
        print(' '*(n-i),end="")
        print('*'*(i*2-1))
    else:
        print(' '*(i-n),end="")
        print('*'*((2*n)-(((i-n)*2)+1)))