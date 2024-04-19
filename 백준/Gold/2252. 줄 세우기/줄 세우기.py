from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
id = [0] * (N + 1)
q = deque()
ans = []

for _ in range(M):  # M명의 학생이 노드
    A, B = map(int, input().split())
    adj[A].append(B)
    id[B] += 1

for i in range(1, N + 1):
    if id[i] == 0:
        q.append(i)  # 들어오는 간선이 없는 노드면 큐에 삽입

while q:
    student = q.popleft()
    ans.append(student)

    for s in adj[student]:
        id[s] -= 1
        if id[s] == 0:
            q.append(s)
print(*ans)