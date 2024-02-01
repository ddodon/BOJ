from collections import deque  # defaultdict -> 시간초과 / 덱 + 10만개 배열로 수정


def bfs(n, m):
    v = [0] * 100_001
    q = deque()
    v[n] = 1
    q.append(n)

    while q:
        c = q.popleft()
        if c == m:
            return v[c] - 1
        for new in (c - 1, c + 1, c * 2):
            if 0 <= new <= 100_000 and v[new] == 0: #조건 Index 주의 + and 연산 앞 범위 신경쓰기
                v[new] = v[c] + 1
                q.append(new)


N, M = map(int, input().split())
print(bfs(N, M))