'''
Memo 18232 텔레포트 정거장
방문배열에 거리 삽입, 정렬 주의
결과 1) x
BFS는 항상 최단거리...
값을 매번 비교할 필요가 없다...
'''
import sys
from collections import deque

input = sys.stdin.readline


def bfs(s):
    q = deque()
    q.append((s, 0))
    v = [0 for _ in range(N + 1)]
    v[s] = 1
    while q:
        c, t = q.popleft()
        for nc in (c - 1, c + 1, *lst[c]):
            if 0 < nc <= N and not v[nc]:
                if nc == E:
                    print(t + 1)
                    return
                q.append((nc, t + 1))
                v[nc] = 1
    return


N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]

S, E = map(int, input().split())
for _ in range(M):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)
bfs(S)