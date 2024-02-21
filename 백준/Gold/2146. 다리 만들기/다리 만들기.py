'''
Memo BOJ 2146 다리만들기
섬은 항상 2개 이상 존재
1) 육지마다 번호 부여
2) 육지 끄트머리에서 BFS 탐색 시작
3) 출발 육지 번호와 다른 번호의 육지를 만났을 때 종료
4) 최단 거리 출력 
* 최단거리보다 더 깊이 가는 경우 가지치기
'''
from collections import deque

# 방향
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


# 육지판별 BFS
def bfs(si, sj, cnt):
    q = deque()
    q.append((si, sj))
    v_land[si][sj] = cnt
    while q:
        ci, cj = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and v_land[ni][nj] == 0 and arr[ni][nj] == 1:
                v_land[ni][nj] = cnt
                q.append((ni, nj))
    return 1


# 다리길이 BFS
def bridge(si, sj, long, land_num):
    global ans
    q = deque()
    q.append((si, sj, long))
    v_bridge[si][sj] = long
    while q:
        ci, cj, cl = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            # 범위 내 + 바다X + 다른 육지
            if 0 <= ni < N and 0 <= nj < N and v_land[ni][nj] != land_num and v_land[ni][nj] != 0:
                ans = min(cl, ans)
            elif 0 <= ni < N and 0 <= nj < N and v_land[ni][nj] == 0 and v_bridge[ni][nj] == 0:
                long = cl + 1
                if long > ans:
                    return
                v_bridge[ni][nj] = 1
                q.append((ni, nj, long))
    return 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 육지 번호 표시 배열 / 육지 번호
v_land = [[0 for _ in range(N)] for _ in range(N)]
cnt = 1

# 타 육지 도착 최단거리
ans = N ** 2

# 육지 판별
for i in range(N):
    for j in range(N):
        if v_land[i][j] == 0 and arr[i][j] == 1:
            if bfs(i, j, cnt):
                cnt += 1

# 다리 길이
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            for k in range(len(di)):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                    long = 0
                    # 다리 방문 표시 배열 초기화
                    v_bridge = [[0 for _ in range(N)] for _ in range(N)]
                    if bridge(i, j, long, v_land[i][j]):
                        pass
# for lst in v_bridge:
#     print(lst)
# print(ans)
print(ans)
