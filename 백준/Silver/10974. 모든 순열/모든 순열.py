def dfs(n,tlst):
    if n == N:
        print(*tlst)
        return
    for i in range(1,N+1):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1,tlst+[i])
            v[i] = 0

N = int(input())
v = [0]*(N+1) # 중복 수 확인
dfs(0,[]) # (n, tlst)