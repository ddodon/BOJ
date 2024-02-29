def dfs(n, w):
    global ans
    if n == N:
        if w >= 500:
            ans += 1
        return

    if w < 500:
        return

    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            w = w + lst[i] - K
            dfs(n + 1, w)
            v[i] = 0
            w = w - lst[i] + K

# 운동키트 / 중량감소량
N, K = map(int, input().split())
lst = list(map(int, input().split()))

v = [0] * (N)
w = 500
ans = 0

dfs(0, w)
print(ans)