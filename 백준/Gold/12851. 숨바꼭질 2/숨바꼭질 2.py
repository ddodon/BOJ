from collections import deque
def bfs(n,k):
    q = deque()
    v = [0]*100_001
    time = -1
    q.append(n)
    v[n] = 1
    way = 0
    while q:
        c = q.popleft()
        if c == k:
            time = v[c]-1
            way += 1
            continue
        for n in (c-1, c+1, c*2):
            if 0<=n<=100_000 and (v[n]==0 or v[n] == v[c] + 1):
                q.append(n)
                v[n] = v[c] + 1
    return time, way
N, K = map(int, input().split())

if N == K: #같은 위치에 있는 경우
    print(0)
    print(1)
else:
    res = bfs(N,K)
    print(res[0])
    print(res[1])