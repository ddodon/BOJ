# 시간복잡도 비교 (tornado 함수 호출 시)
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
ai = [[-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],
      [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],
      [2, 1, 1, 1, 0, -1, -1, -1, -2, 0],
      [0, -1, 0, 1, -2, -1, 0, 1, 0, -1]]
aj = [[0, -1, 0, 1, -2, -1, 0, 1, 0, -1],
      [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],
      [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],
      [2, 1, 1, 1, 0, -1, -1, -1, -2, 0]]
ratio = [0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02, 0]

def tornado(ci, cj, d):
    global ans
    s = arr[ci][cj]
    arr[ci][cj]=0
    sm = 0
    for loc in range(10):
        ni, nj = ci + ai[d][loc], cj + aj[d][loc]
        t = int(s * ratio[loc])
        if loc == 9:
            t = s-sm
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += t
        else:
            ans += t
        sm += t


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ci, cj = N // 2, N // 2
d = 0
cnt = 0  # 지나온 칸
hold = 1  # 지나가는 칸
flag = 0  # 지나가는 칸 개수 늘리기
ans = 0  # 격자 밖으로 나간 모래
# 달팽이
while 1:
    if (ci, cj) == (0, 0):
        break
    ni = ci + di[d]
    nj = cj + dj[d]
    tornado(ni, nj, d)
    cnt += 1
    ci, cj = ni, nj
    if cnt == hold:
        flag += 1
        if flag == 2:
            d = (d + 1) % 4
            flag = 0
            cnt = 0
            hold += 1
        else:
            d = (d + 1) % 4
            cnt = 0
print(ans)