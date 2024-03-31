di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def dfs(n, orders):
    global ans
    if n == 5:
        trr = [lst[::] for lst in arr]
        for order in orders:
            trr = play(trr, order)
        ans = max(ans, max(map(max, trr)))
        return
    for j in range(len(di)):
        dfs(n + 1, orders + [j])

def play(arr, d):
    # 위, 왼쪽
    v_set = set()  # 이미 합쳐진 좌표
    if d == 0 or d == 3:
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0:
                    continue
                ci, cj = i, j
                while 1:
                    ni = ci + di[d]
                    nj = cj + dj[d]
                    if not (0 <= ni < N and 0 <= nj < N):
                        break
                    elif arr[ni][nj] == 0:
                        arr[ci][cj], arr[ni][nj] = arr[ni][nj], arr[ci][cj]
                        ci, cj = ni, nj
                    elif arr[ni][nj] == arr[ci][cj]:
                        if (ni,nj) in v_set:
                            break
                        arr[ci][cj] = 0
                        arr[ni][nj] *= 2
                        v_set.add((ni,nj))
                    elif arr[ni][nj] != arr[ci][cj]:
                        break

    # 아래, 오른쪽
    else:
        if d == 1 or d == 2:
            for i in range(N-1,-1,-1):
                for j in range(N-1,-1,-1):
                    if arr[i][j] == 0:
                        continue
                    ci, cj = i, j
                    while 1:
                        ni = ci + di[d]
                        nj = cj + dj[d]
                        if not (0 <= ni < N and 0 <= nj < N):
                            break
                        elif arr[ni][nj] == 0:
                            arr[ci][cj], arr[ni][nj] = arr[ni][nj], arr[ci][cj]
                            ci, cj = ni, nj
                        elif arr[ni][nj] == arr[ci][cj]:
                            if (ni, nj) in v_set:
                                break
                            arr[ci][cj] = 0
                            arr[ni][nj] *= 2
                            v_set.add((ni, nj))
                            break
                        elif arr[ni][nj] != arr[ci][cj]:
                            break
    return arr

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0  # 가장 큰 블럭의 수
dfs(0, [])
print(ans)