from collections import deque

di = [-1,0,1,0]
dj = [0,1,0,-1]

def bfs(si,sj):
    change = 1
    q = deque()
    q.append((si,sj,change))
    v = [[21e8]*(N) for _ in range(N)]
    v[si][sj] = 1

    while q:
        ci,cj,cc = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0<=ni<N and 0<=nj<N and v[ni][nj]>cc:
                if arr[ni][nj] == 1:
                    q.append((ni,nj,cc))
                    v[ni][nj]=cc
                elif arr[ni][nj] == 0:
                    q.append((ni,nj,cc+1))
                    v[ni][nj]=cc+1
    return v[ei][ej]-1
N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
si,sj,ei,ej = 0,0,N-1,N-1
ans = bfs(si,sj)
print(ans)