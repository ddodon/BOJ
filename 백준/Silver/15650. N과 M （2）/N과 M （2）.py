def dfs(n,s,tlst):
    if n == M:
        print(*tlst)
        return
    for j in range(s+1,N+1):
        dfs(n+1,j,tlst+[j]) #스타팅 포인트 이후
N, M = map(int,input().split())
lst = [i for i in range(1,N+1)]
ans = []
dfs(0,0,ans) # (root, start_in, answer)