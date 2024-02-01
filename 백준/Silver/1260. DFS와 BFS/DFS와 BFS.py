def bfs(V):
    q = []
    v = [0 for _ in range(N+1)]
    ans = []
    q.append(V)
    v[V] = 1
    ans.append(V)
    while q:
        c = q.pop(0)
        for n in adj[c]:
            if v[n] == 0:
                v[n] = 1
                q.append(n)
                ans.append(n)
    return ans

def dfs(V):
    dfs_v[V]=1
    dfs_ans.append(V)
    for n in adj[V]:
        if dfs_v[n] == 0:
            dfs(n)


N, M, V = map(int, input().split())
adj = [ [] for _ in range(N+1)]
dfs_v = [0 for _ in range(N+1)]
dfs_ans = [] #dfs 재귀

for i in range(M):
    s,e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)
for lst in adj:
    lst.sort() # 작은 순으로 방문

ans_bfs = bfs(V)
dfs(V)

print(*dfs_ans)
print(*ans_bfs)