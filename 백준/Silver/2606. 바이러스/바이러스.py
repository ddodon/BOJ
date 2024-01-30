def dfs(c):
    v[c] = 1
    ans.append(c)
    for n in adj[c]:
        if v[n] == 0:
            dfs(n)

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
v = [0 for _ in range(N+1)]
ans = []
for i in range(M):
    s,e = map(int,input().split())
    adj[e].append(s)
    adj[s].append(e)
dfs(1)
print(len(ans)-1) #1번 콤퓨타 제외