'''
Memo Boj 2636 치즈
현재 위치가 공기(0)이고, 다음 탐색 위치가 1(치즈)면 0으로 변환
-> 이 로직을 bfs안에 삽입
'''
from collections import deque
#방향: 상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]

def air_bfs(i,j):
    q = deque()

    # i좌표, j좌표,
    q.append((i,j))
    v[i][j] = 1
    cnt = 0
    while q:
        ci,cj = q.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0<= ni < N and 0<=nj<M and v[ni][nj] == 0:
                # 다음이 공기라면
                if arr[ni][nj] == 0:
                    v[ni][nj] = 1
                    q.append((ni,nj))
                # 다음 치즈라면
                elif arr[ni][nj] == 1:
                    v[ni][nj] = 1
                    arr[ni][nj] = 0 #치즈 녹음
                    cnt += 1
    return cnt


N,M = map(int,input().split())
# 주어진 치즈
arr = [list(map(int,input().split())) for _ in range(N)]

# 시간
t = 0
# 시간별 남은 치즈
ans = []
# 공기 탐색 bfs
while 1:
    t += 1
    v = [[0 for _ in range(M)] for _ in range(N)]
    cnt = air_bfs(0,0)

    # 녹일 치즈 없음
    if cnt == 0:
        break
    else:
        ans.append(cnt)
if ans:
    print(len(ans))
    print(ans[-1])
else:
    print(0)
    print(0)