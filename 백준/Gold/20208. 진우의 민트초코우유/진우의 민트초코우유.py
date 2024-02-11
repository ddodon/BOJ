'''
Memo BOJ 20208 진우의 민트초코우유
* 우유의 위치 파악 + 우유에 도달 했을 때 집에 갈 수 있는 체력이라면 현재까지 모은 우유를 갱신
'''
# 현재 위치 / 남은 체력
def dfs(ci,cj,m):
    global cnt
    global ans

    # 종료 조건: 모든 우유 좌표에 방문해보는 경우의 수
    for i in range(len(milks)):
        mi = milks[i][0]
        mj = milks[i][1]
        dist = abs(mi-ci) + abs(mj-cj)
        # 마신 적 없는 우유 + 체력 내 도달 가능
        if v[i] == 0 and dist <= m:
            v[i] = 1
            cnt += 1
            m = m - dist + H
            dfs(mi,mj,m)
            v[i] = 0 # 원상복구
            cnt -= 1
            m = m + dist - H

        # 정답조건: 현재 좌표에서 집으로 돌아올 때까지의 마신 우유의 양
        if (abs(ci - si) + abs(cj - sj)) <= m:
            ans = max(ans, cnt)


N,M,H = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
milks = [] # 민초우츄 좌표
for i in range(N):
    for j in range(N):
        # 진우네 좌표 체크
        if arr[i][j] == 1:
            si, sj = i,j
        # 민초우유 좌표 추가
        elif arr[i][j] == 2:
            milks.append((i,j))

# 마신 우유 체크 배열 / 마신 우유 개수
v = [0 for _ in range(len(milks))]
ans = cnt = 0

dfs(si,sj,M)
print(ans)