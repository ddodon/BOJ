'''
Memo BOJ N과M 12
N개의 자연수 중 M개 선택 *(서로 같은 수 있음)
중복 X + 순서 O

*숫자가 적힌 만큼만 활용 idx+1
*숫자를 순서가 의미를 가지게 활용 idx
'''


def dfs(n, idx, tlst):
    # 종료조건
    if n == M:
        print(*tlst)
        return

    # N개의 자연수 중 서로 같은 수가 있어 중복 되는 경우 방지
    tmp = -1
    for i in range(idx, N):
        if tmp != lst[i]:
            tmp = lst[i]
            tlst.append(lst[i])
            dfs(n + 1, i, tlst)
            tlst.pop()


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []
dfs(0, 0, [])
