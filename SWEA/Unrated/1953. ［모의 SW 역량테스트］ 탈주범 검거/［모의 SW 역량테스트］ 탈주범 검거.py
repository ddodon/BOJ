from collections import deque

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]
opp = {1: 2, 2: 1, 3: 4, 4: 3}
dir = [[], [1, 2, 3, 4], [1, 2], [3, 4], [1, 4], [2, 4], [2, 3], [1, 3]]


def bfs(si, sj, L):
    q = deque()
    q.append((si, sj))
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        if v[ci][cj] == L:
            break
        for d in dir[arr[ci][cj]]:
            ni = ci + di[d]
            nj = cj + dj[d]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] > 0:
                if opp[d] in dir[arr[ni][nj]]:
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj] + 1
                    cnt += 1
    return cnt

T = int(input())
for test_case in range(1, T + 1):
    # 세로 / 가로 / 맨홀 좌표 / 소요 시간 L
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(R, C, L)
    print(f'#{test_case} {ans}')