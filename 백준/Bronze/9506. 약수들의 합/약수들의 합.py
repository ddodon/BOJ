while 1:
    lst = [] #약수를 담을 리스트
    n = int(input())
    if n == -1:break
    for i in range(1,int((n/2)+1)):
        if n % i == 0:
            lst.append(i)
    if n == sum(lst):
        print(f'{n} =',end="")
        for i in range(len(lst)):
            print(f' {lst[i]}',end="")
            if i < len(lst)-1:
                print(" +",end="")
        print()
    else:
        print(f'{n} is NOT perfect.')