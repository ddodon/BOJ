'''
Memo BOJ N과M 5
N개의 자연수 중 M개 선택
중복 방지 + 순서 O
'''


def dfs(n, tlst):
    if n == M:
        print(*tlst)
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            tlst.append(lst[i])
            dfs(n + 1, tlst)
            tlst.pop()
            v[i] = 0


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
v = [0] * (N)
dfs(0, [])