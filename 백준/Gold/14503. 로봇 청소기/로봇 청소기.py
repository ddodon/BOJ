'''
Memo Boj 14503 로봇 청소기
정지조건: 주변 4칸 청소완료(/불가능) 후 후진 시 벽
1차 해멨던 부분: ni, nj 범위 설정
'''
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [[1] * (M + 2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1] * (M + 2)]
# 0: 청소 X
# 1: 벽
# 2: 청소 O

ci, cj = r + 1, c + 1

ans = 0
while 1:
    # 1. 현재 칸 청소 x
    if arr[ci][cj] == 0:
        arr[ci][cj] = 2
        ans += 1
        # 2. 현재 칸 주변 4칸 탐색
    if any([(arr[ci - 1][cj] == 0), (arr[ci][cj + 1] == 0), \
            (arr[ci + 1][cj] == 0), (arr[ci][cj - 1] == 0)]):
        # 빈 칸 O
        d = (d - 1) % 4
        ni = ci + di[d]
        nj = cj + dj[d]
        if 0 <= ni <= N + 1 and 0 <= nj <= M + 1 and arr[ni][nj] == 0:
            ci = ni
            cj = nj

    # 빈 칸 x
    else:
        ni = ci - di[d]
        nj = cj - dj[d]
        if 0 <= ni <= N + 1 and 0 <= nj <= M + 1:
            if arr[ni][nj] == 1:  # 작동 중지
                print(ans)
                exit()
                break
            else:  # 1칸 후진
                ci = ci - di[d]
                cj = cj - dj[d]