def dfs(n,cost):
    global mx
    # 종료조건
    if n == N:
        mx = max(mx,cost)
        return

    # 날짜 선택
    if v[n] == 0 and n + day[n] <=N:
        cost += money[n]
        for i in range(day[n]):
            v[n+i]=1
        dfs(n+1,cost)
        for i in range(day[n]):
            v[n + i] = 0
        cost -= money[n]
    dfs(n+1,cost)

    # 날짜 미선택

N = int(input())
day=[]
money=[]
v = [0]*(N+5)
mx = 0
for _ in range(N):
    d, m = map(int,input().split())
    day.append(d)
    money.append(m)

dfs(0,0)
print(mx)