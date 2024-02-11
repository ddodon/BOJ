'''
Memo BOJ 16509 장궁
상이 가는 경로에 왕이 있으면 안됨 + 억지 하드코딩
'''
from collections import deque

# 상의 이동방향
di = [-3,-2,2,3,3,2,-2,-3]
dj = [2,3,3,2,-2,-3,-3,-2]
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.popleft()
        # 종료조건
        if (ci,cj) == (ei,ej):
            return v[ci][cj]-1
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            # 범위 내 + 미방문
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0:
                #상의 이동 경로 내 왕이 있는 경우
                if k == 0:
                    if (ci-1,cj)==(ei,ej) or (ci-2,cj+1)==(ei,ej):
                        continue
                elif k == 1:
                    if (ci,cj+1)==(ei,ej) or (ci-1,cj+2)==(ei,ej):
                        continue
                elif k == 2:
                    if (ci,cj+1)==(ei,ej) or (ci+1,cj+2)==(ei,ej):
                        continue
                elif k == 3:
                    if (ci+1,cj)==(ei,ej) or (ci+2,cj+1)==(ei,ej):
                        continue
                elif k == 4:
                    if (ci+1,cj)==(ei,ej) or (ci+2,cj-1)==(ei,ej):
                        continue
                elif k == 5:
                    if (ci,cj-1)==(ei,ej) or (ci+1,cj-2)==(ei,ej):
                        continue
                elif k == 6:
                    if (ci,cj-1)==(ei,ej) or (ci-1,cj-2)==(ei,ej):
                        continue
                elif k == 7:
                    if (ci-1,cj)==(ei,ej) or (ci-2,cj-1)==(ei,ej):
                        continue
                v[ni][nj] = v[ci][cj]+1
                q.append((ni,nj))

N,M=10,9
si, sj = map(int,input().split())
ei, ej = map(int,input().split())
arr = [[0]*M for _ in range(N)]
v = [[0]*M for _ in range(N)]

ans = bfs(si,sj)
# for lst in v:
#     print(lst) # 경로 확인용
print(ans)