def dfs(n,s,slst):
    global cnt
    # 가지치기: 난이도의 합이 R보다 큰 경우
    if sum(slst) > R:
        return
    # 정답조건: 2문제 이상
    if len(slst) >= 2:
        if sum(slst) >= L and (max(slst)-min(slst)>=X):
            cnt += 1
    # 종료조건
    if n == N:
        return
    for i in range(s,N):
        if v[i] == 0:
            v[i] = 1
            slst.append(lst[i])
            dfs(n+1,i,slst)
            v[i] = 0
            slst.pop()
N, L, R, X = map(int,input().split())
lst = list(map(int,input().split()))
v = [0]*N
cnt = 0
# print(N, L, R, X,"배열:",lst)
# 백트래킹 (n, sum_lst: 캠프용 문제 배열)
dfs(0,0,[])
print(cnt)