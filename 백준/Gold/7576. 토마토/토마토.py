from collections import deque
# 덱을 써야 시간초과가 안난다고 한다...

#방향: 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(tmt,cnt):
    v = [[0]*M for _ in range(N)]
    d = deque()
    ans = [] #디버깅용 순서배열
    t= 0 #날짜
    count = 0
    for si, sj in tmt: #토마토 익은거 마다
        v[si][sj] = 1
        d.append((si,sj,t))
    while d:
        for _ in range(len(d)):
            c = d.popleft() #덱 활용
            if cnt == count: #토마토가 모두 익었다.
                return ans[-1][2]
            for k in range(len(di)): #사방
                ni = c[0] + di[k]
                nj = c[1] + dj[k]
                if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and tomato[ni][nj] == 0:
                    v[ni][nj] = c[2]+1
                    d.append((ni,nj,c[2]+1))
                    ans.append((ni,nj,c[2]+1))
                    count += 1
    return -1

M,N = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]
tmt = [] #익어있는 토마토 리스트
cnt = 0 #설익은 토마토 개수
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            tmt.append((i, j))
        elif tomato[i][j] == 0:
            cnt += 1
if cnt == 0:
    print(0)
else:
    res = bfs(tmt,cnt) #익은 토마토 리스트
    print(res)