from collections import deque
def bfs(s,num):
    q = deque()
    q.append(s)
    if v[s] != 0:
        return

    while q:
        c = q.popleft()
        for n in adj[c]:
            if v[n] == 0:
                v[n] = num
                q.append(n)
    return v

N, M = map(int,input().split())
adj = [[] for _ in range(N+1)]
v = [0] * (N + 1)
for _ in range(M):
    s,e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)
for lst in adj:
    lst.sort()
for i in range(1,N+1): #정점 1부터
    bfs(i,i)
alone = v[1:].count(0) # 간선없는 노드 개수
together = len(set(v))-1 #연결된 노드 묶음
print(alone+together)