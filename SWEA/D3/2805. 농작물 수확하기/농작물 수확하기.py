T = int(input())
N = []
for test_case in range(1, T + 1):
    n = int(input())
    res = 0 # 총합
    t = n//2
    north = 0
    south = 1
    arr = [input() for _ in range(n)]
    for i in range(n):
        if i < t:
            for k in range(t-north,t+north+1):
                res += int(arr[i][k])
            north += 1
        elif i == t:
            for j in range(n):
                res += int(arr[i][j])
        else:
            for k in range(south, n-south):
                res += int(arr[i][k])
            south += 1
    print(f'#{test_case} {res}')