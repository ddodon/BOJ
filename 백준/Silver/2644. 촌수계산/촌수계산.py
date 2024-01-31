def bfs(s,e):
    v = [0 for _ in range(N+1)]
    q = []
    ans = []

    ans.append(s) #임시 순서 기록용
    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        if c == e:
            return v[c]-1
        for n in adj[c]:
            if v[n] == 0:
                v[n] = v[c] + 1
                q.append(n)
                ans.append(n)
    return -1


N = int(input())
S, E = map(int,input().split())
M = int(input())
adj = [ [] for _ in range(N+1)] #촌수 알아볼 배열
for i in range(M):
    s, e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)
res = bfs(S,E)
print(res)