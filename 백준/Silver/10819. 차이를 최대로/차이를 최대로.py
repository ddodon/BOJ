def dfs(n, tlst):
    global ans
    sm = 0
    if n == N: # N개 선택 완료
        for i in range(1,N):
            sm += abs(tlst[i-1]-tlst[i])
        if ans < sm:
            ans = sm
        else:
            sm = 0
        return
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            tlst.append(lst[j])
            dfs(n+1,tlst)
            tlst.pop()
            v[j] = 0

N = int(input())
lst = list(map(int,input().split()))
ans = 0 # 문제의 최댓값
v = [0] * N
dfs(0,[]) #(n, sum lst)
print(ans)