def dfs(n, tlst):
    if n == M:
        print(*tlst)
        return

    for i in range(N):
        if v[i] == 0:
            v[i]=1
            tlst.append(i+1)
            dfs(n+1,tlst)
            tlst.pop(-1)
            v[i]=0

N, M = map(int,input().split())
v = [0]*(N)
dfs(0,[])