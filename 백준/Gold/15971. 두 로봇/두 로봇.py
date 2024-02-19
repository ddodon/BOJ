import sys
sys.setrecursionlimit(100000)
def dfs(s, sm, mx):
    if s == R2:
        print(sm - mx)
        exit(0)
    v[s] = 1
    for e, w in adj[s]:
        if v[e] == 0:
            dfs(e, sm + w, max(mx, w))

# 방 개수 / 방1 / 방2
N, R1, R2 = map(int, input().split())
adj = [[] for _ in range(N + 1)]
v = [0 for _ in range(N + 1)]
sm = mx = 0

for i in range(N - 1):
    # 방s / 방e / 길이
    s, e, w = map(int, input().split())
    adj[s].append((e, w))
    adj[e].append((s, w))
dfs(R1, 0, mx)