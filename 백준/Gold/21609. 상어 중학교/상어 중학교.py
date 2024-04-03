from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj, num):
    q = deque()
    q.append((si, sj))
    v = [[0] * N for _ in range(N)]
    v[si][sj] = 1
    same = [(si, sj)]  # 그룹에 포함된 블럭 좌표
    rainbow_block = 0  # 무지개블럭 개수

    while q:
        ci, cj = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if (0 <= ni < N and 0 <= nj < N) and v[ni][nj] == 0:
                if arr[ni][nj] == num:  # 같은 색 블록
                    q.append((ni, nj))
                    v[ni][nj] = 1
                    v_main[ni][nj] = 1
                    same.append((ni, nj))
                elif arr[ni][nj] == 0:  # 무지개 블럭
                    q.append((ni, nj))
                    v[ni][nj] = 1
                    same.append((ni, nj))
                    rainbow_block += 1
    return (len(same), rainbow_block, same[0][0], same[0][1], same)


def gravity(arr):
    for i in range(N - 2, -1, -1):
        for j in range(N - 1, -1, -1):
            if arr[i][j] < 0: continue
            ci, cj = i, j
            while 1:
                ni = ci + 1
                if 0 <= ni < N and arr[ni][cj] == -2:
                    arr[ni][cj], arr[ci][cj] = arr[ci][cj], arr[ni][cj]
                    ci = ni
                else:
                    break
    return arr


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 블록그룹이 있는 동안
while 1:
    # 1. 블럭 집합 찾기
    groups = []
    v_main = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and v_main[i][j] == 0:
                res = bfs(i, j, arr[i][j])
                # 집합개수, 무지개블럭 개수, 기준블럭좌표, 블럭좌표
                if res[0] < 2: continue
                groups.append(res)

    # 블럭집합 없으면 끝
    if not groups: break

    # 가장 큰 블럭
    groups.sort(reverse=True)
    cnt, rainbow, std_i, std_j, blocks = groups[0]
    ans += cnt ** 2
    for bi, bj in blocks:
        arr[bi][bj] = -2

    # 3. 중력1
    arr = gravity(arr)

    # 4. 격자 반시계 회전
    arr = [list(lst) for lst in zip(*arr)][::-1]

    # 5. 중력2
    arr = gravity(arr)

print(ans)