di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

ti = [-2, -1, -1, -1, 0, 1, 1, 1, 2]
tj = [0, -1, 0, 1, -2, -1, 0, 1, 0]

ratio = [0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02]

def tornado(ci, cj, d):
    global ans
    s = arr[ci][cj]
    if d == 0:
        for k in range(len(ti)):
            ni = ci + ti[k]
            nj = cj + tj[k]
            sand = int(s * (ratio[k]))
            if 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj] += sand
                arr[ci][cj] -= sand
            else:
                ans += sand
                arr[ci][cj] -= sand
        ni = ci + 0
        nj = cj + (-1)
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += arr[ci][cj]
            arr[ci][cj] = 0
        else:
            ans += arr[ci][cj]
            arr[ci][cj] = 0

    elif d == 1:
        for k in range(len(ti)):
            ni = ci - tj[k]
            nj = cj + ti[k]
            sand = int(s * (ratio[k]))
            if 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj] += sand
                arr[ci][cj] -= sand
            else:
                ans += sand
                arr[ci][cj] -= sand
        ni = ci + 1
        nj = cj + 0
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += arr[ci][cj]
            arr[ci][cj] = 0
        else:
            ans += arr[ci][cj]
            arr[ci][cj] = 0

    elif d == 2:
        for k in range(len(ti)):
            ni = ci + ti[k]
            nj = cj - tj[k]
            sand = int(s * (ratio[k]))
            if 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj] += sand
                arr[ci][cj] -= sand
            else:
                ans += sand
                arr[ci][cj] -= sand
        ni = ci + 0
        nj = cj + 1
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += arr[ci][cj]
            arr[ci][cj] = 0
        else:
            ans += arr[ci][cj]
            arr[ci][cj] = 0

    elif d == 3:
        for k in range(len(ti)):
            ni = ci + tj[k]
            nj = cj - ti[k]
            sand = int(s * (ratio[k]))
            if 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj] += sand
                arr[ci][cj] -= sand
            else:
                ans += sand
                arr[ci][cj] -= sand
        ni = ci - 1
        nj = cj + 0
        if 0 <= ni < N and 0 <= nj < N:
            arr[ni][nj] += arr[ci][cj]
            arr[ci][cj] = 0
        else:
            ans += arr[ci][cj]
            arr[ci][cj] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ci, cj = N // 2, N // 2
d = 0
cnt = 0  # 지나온 칸
hold = 1  # 지나가는 칸
flag = 0  # 지나가는 칸 개수 늘리기
ans = 0  # 격자 밖으로 나간 모래
while 1:
    if (ci, cj) == (0, 0):
        break
    ni = ci + di[d]
    nj = cj + dj[d]
    tornado(ni, nj, d)

    cnt += 1
    ci, cj = ni, nj
    # 방향이동
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