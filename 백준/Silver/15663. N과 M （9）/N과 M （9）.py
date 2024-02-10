'''
Memo BOJ N과M 9
N개의 자연수 중 M개 선택 *(서로 같은 수 있음)
중복 X + 순서 X
'''


def dfs(n, tlst):
    if n == M:
        print(*tlst)
        return
    # 직전에 뽑힌 수
    tmp = -1
    for i in range(N):
        if v[i] == 0 and lst[i] != tmp:
            v[i] = 1
            tmp = lst[i]
            tlst.append(lst[i])
            dfs(n + 1, tlst)
            tlst.pop()
            v[i] = 0


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
v = [0] * N
ans = []
dfs(0, [])