'''
Memo BOJ 16928 뱀과 사다리 게임
사다리와 뱀을 타고 내려가거나 올라갈 수 있는 최단거리 문제 (BFS
사다리를 타는 것이 무조건 유리할까?
'''

from collections import defaultdict
from collections import deque
# 현재 위치 (출발위치)
def bfs(s):
    q = deque()
    q.append(s)
    # 1 -> 시작포인트 (던진횟수: 0)
    v[s] = 0

    while q:
        c = q.popleft()
        if c == 100:
            break

        #주사위 던지기 (6부터)
        for i in range(1,7):
            n = c+i
            # 이동하려는 곳에 사다리나 뱀
            if n in ladder.keys():
                n = ladder[n]
            if n in snake.keys():
                n = snake[n]
            # 범위 내 / 미방문
            if n <= 100 and v[n] == 0:
                v[n] = v[c]+1
                q.append(n)

N, M = map(int, input().split())
# 사다리 / 뱀 위치 배열
ladder = defaultdict(int)
snake = defaultdict(int)
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    x, y = map(int, input().split())
    snake[x] = y

# 게임보드 방문 체크 및 위치별 최단거리
v = [0 for _ in range(101)]
# BFS
bfs(1)
print(v[100])