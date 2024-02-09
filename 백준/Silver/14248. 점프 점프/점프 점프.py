'''
Memo Boj 14248 점프 점프
BFS
'''
from collections import deque
def bfs(s): #시작 idx
    q = deque()
    q.append(s)
    v[s] = 1
    cnt = 1
    while q:
        c = q.popleft()
        nc = c + lst[c]
        mc = c - lst[c]
        if 0 < nc <= N and v[nc] == 0:
            v[nc] = 1
            q.append(nc)
            cnt += 1
        if 0 < mc <= N and v[mc] == 0:
            v[mc] = 1
            q.append(mc)
            cnt += 1
    return cnt
N = int(input())
lst = list(map(int,input().split()))
S = int(input())
v = [0] * (N+1)
lst.insert(0,0)

cnt = bfs(S)
print(cnt)