'''
Memo Boj 
메모리:
시간:
결과:  (/3)
풀이시간: 
▷ 문제 읽기: 12분
▷ 풀이 구상: 분
▷ 로직 구현: 
    - 단계별로 나눠서 구현 (1~3단계부터 구상 후 구현) (슬라이싱 전치행렬)
▷ 오류 수정: 
    - 100분: 마지막 TC 1 안맞음(ans-> 13, 나->12)
    - 180분: 도저히 못찾겠음
    - 206분: 오류 발견 - 온도 조절부분 좌표 참조
    - 210분: indexerror 디버깅하면서 이리 저리 손대다가 범위 실수 (regulate2 함수)
▷ 오류 부분: 
'''

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def stack_tank(lst):
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


def regulate(arr):
    nrr = [[0] * len(arr[-1]) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            nrr[i][j] += arr[i][j]
    nnrr = [x[:] for x in nrr]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if not arr[i][j]: continue
            ci, cj = i, j
            for k in range(len(di)):
                ni = ci + di[k]
                nj = cj + dj[k]
                if 0 <= ni < len(arr) and 0 <= nj < len(arr[i]) and nnrr[ci][cj] > nnrr[ni][nj] and nrr[ni][nj]:
                    d = (arr[ci][cj] - arr[ni][nj]) // 5
                    nrr[ci][cj] -= d
                    nrr[ni][nj] += d
    return nrr

def regulate2(arr):
    nrr = [x[:] for x in arr]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            ci, cj = i, j
            for k in range(len(di)):
                ni = ci + di[k]
                nj = cj + dj[k]
                if 0 <= ni < len(arr) and 0 <= nj <len(arr[0]) and arr[ci][cj] > arr[ni][nj]:
                    d = (arr[ci][cj] - arr[ni][nj]) // 5
                    nrr[ci][cj] -= d
                    nrr[ni][nj] += d
    return nrr

def line(arr):
    arr = [list(x) for x in zip(*arr[::-1])]
    lst = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]:
                lst.append(arr[i][j])
    return lst


def stack_tank2(lst):
    m = len(lst) // 2
    up = lst[:m][::-1]
    down = lst[m:]

    arr = []
    arr.append(up[:m // 2])
    up = up[m // 2:]
    arr.append(down[:m // 2])
    down = down[m // 2:]
    arr = [list(x) for x in zip(*arr[::-1])]
    arr = [list(x) for x in zip(*arr[::-1])]
    arr.append(up)
    arr.append(down)
    return arr


N, K = map(int, input().split())
fishtank = list(map(int, input().split()))

ans = 0
while 1:
    mn = min(fishtank)
    mx = max(fishtank)

    if mx - mn <= K:
        break

    for i in range(len(fishtank)):
        if fishtank[i] == mn: fishtank[i] += 1

    arr = stack_tank(fishtank)
    arr = regulate(arr)
    fishtank = line(arr)
    arr = stack_tank2(fishtank)
    arr = regulate2(arr)
    fishtank = line(arr)
    # print2(arr)
    ans += 1
print(ans)