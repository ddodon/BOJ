# stack 부분만 바꿔봄
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def stack(lst):
    idx = 1
    arr = []
    arr.append(lst[:idx])
    lst = lst[idx:]
    while 1:
        idx = len(arr[0])
        arr.append(lst[:idx])
        lst = lst[idx:]
        arr = [list(x) for x in zip(*arr[::-1])]
        if len(arr) + 1 > len(lst) - len(arr[0]):
            break
    arr.append(lst)
    return arr


def adjust(arr):
    nrr = [lst[::] for lst in arr]
    been = set()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ci, cj = i, j
            for k in range(len(di)):
                ni = ci + di[k]
                nj = cj + dj[k]
                if 0 <= ni < len(arr) and 0 <= nj < len(arr[ni]):
                    d = abs(arr[ci][cj] - arr[ni][nj]) // 5
                    if d < 1: continue
                    if (ci, cj, ni, nj) in been: continue
                    been.add((ci, cj, ni, nj))
                    been.add((ni, nj, ci, cj))
                    if arr[ci][cj] > arr[ni][nj]:
                        nrr[ci][cj] -= d
                        nrr[ni][nj] += d
                    elif arr[ci][cj] < arr[ni][nj]:
                        nrr[ci][cj] += d
                        nrr[ni][nj] -= d

    new_list = []
    for j in range(len(nrr[-1])):
        for i in range(len(nrr)-1,-1,-1):
            if j >= len(nrr[i]):continue
            new_list.append(nrr[i][j])
    return new_list


def stack2(lst):
    arr = []
    l = len(lst) // 2
    up = lst[:l][::-1]
    down = lst[l:]

    arr.append(up[:l // 2])
    arr.append(down[:l // 2])
    arr = [list(lst) for lst in zip(*arr[::-1])]
    arr = [list(lst) for lst in zip(*arr[::-1])]
    arr.append(up[l // 2:])
    arr.append(down[l // 2:])
    return arr


N, K = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0  # 어항 정리 횟수

# 어항 정리 시작
while 1:
    mx = max(lst)
    mn = min(lst)
    if mx - mn <= K:
        break

    # 1. 물고기 추가
    for i in range(len(lst)):
        if lst[i] == mn:
            lst[i] += 1

    # 2. 어항 쌓기
    arr = stack(lst)

    # 3. 물고기 조절 + 일렬 정리
    lst = adjust(arr)

    # 4. 어항 쌓기2
    arr = stack2(lst)

    # 5. 물고기 조절 + 일렬 정리
    lst = adjust(arr)

    ans += 1
print(ans)