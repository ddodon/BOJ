def dfs(n,tlst):
    if n == K:
        tmp = int("".join(map(str, tlst)))
        if tmp not in ans:
            ans.append(tmp)
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1 # 자기 자신 인덱스 제외
            tlst.append(lst[i])
            dfs(n + 1, tlst)  # 되돌아 가는 로직
            tlst.pop()
            v[i] = 0

N = int(input())
K = int(input())
lst = []
for _ in range(N):
    tmp = int(input())
    lst.append(tmp)
v = [0] *(N+1)  # 중복 수 확인
ans = []
dfs(0, [])  # (n, key, tlst)
print(len(ans))