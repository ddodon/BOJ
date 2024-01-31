import sys
sys.setrecursionlimit(10000)

# 방향: 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j, v, area):
    if v[i][j] == 1:
        return 0
    v[i][j] = 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:  # 범위 내 + 강우량
            dfs(ni, nj, v, area)
    return 1


N = int(input())
area1 = [list(map(int, input().split())) for _ in range(N)]
# 물에 잠기는 범위: 최소 높이 미만으로 강우 ~ 최대 높이 미만으로 강우

fall = []
for i in range(N):
    for j in range(N):
        fall.append(area1[i][j])
fall.append(min(fall)-1) # 안전지대 1인 경우 추가 ㅠ..ㅠ
fall = set(fall) #강우량 정보
ans = 0
for k in fall:
    v1 = [[0] * N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if area1[a][b] <= k:
                v1[a][b] = 1 #침수된 지역 미리 표시
    cnt = 0
    for i in range(N):
        for j in range(N):
            if dfs(i, j, v1, area1) != 0:
                cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)