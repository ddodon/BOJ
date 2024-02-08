from collections import defaultdict


# 연산의 최솟값 BFS
def bfs(a, b):
    ans = []  # 디버깅용 순서 배열
    q = []
    dic = defaultdict(int) #디폴트딕트로 메모리 절약
    ans.append(a)
    q.append(a)
    while q:
        c = q.pop(0)
        if c == b:
            return dic[b] + 1
        for new in (c * 2, c * 10 + 1):
            if new > b:
                continue
            else:
                q.append(new)
                ans.append(new)
                dic[new] = dic[c] + 1

    return -1


A, B = map(int, input().split())
res = bfs(A, B)
print(res)