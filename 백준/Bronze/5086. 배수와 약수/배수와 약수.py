while 1:
    n, m = map(int,input().split())
    if n == m == 0:
        break

    if n % m == 0: #n이 m의 배수
        print('multiple')
    elif m % n == 0:
        print('factor')
    else:
        print('neither')