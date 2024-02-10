def dfs(n,tlst):
    if n == M:
        print(*tlst)
        return
    for j in range(1,N+1):
        if j not in tlst: #중복 제거
            dfs(n+1,tlst+[j])
N, M = map(int,input().split())
lst = [i for i in range(1,N+1)]
ans = []
dfs(0,ans) # (root, answer)