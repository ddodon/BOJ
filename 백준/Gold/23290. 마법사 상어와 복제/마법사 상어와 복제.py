direction = {0:'←', 1:'↖', 2:'↑', 3:'↗', 4:'→', 5:'↘', 6:'↓', 7:'↙' }

def print_fish(v):
    for x in v:
        for a in x:
            if a:
                print("[",end="")
                for b in a:
                    print(f'{direction[b]}', end=" ")
                print("]",end="")
            else:
                print(f'[  ]', end=" ")
        print()

def print2(v):
    for x in v:
        print(x)
    print()

'''
Memo Boj
메모리:
시간:
결과:  (/)
풀이시간:
▷ 문제 읽기: 12분
▷ 풀이 구상: 분
    - 220분: 머리 멍해짐, 어느 순간 딴 생각하다가 정신차림
    - 상어의 이동은 물고기를 최대한 많이 먹을 수 있는 경로
    - 여러 경로가 있을 경우 이동경로 우선순위 따져봐야 함 (백트래킹 vs 64개 경로 for문)
    - 순서가 그냥 오름차순이나 마찬가지
    - 물고기 냄새는 2 값을 줘버리고 한턴마다 -1씩 할까
▷ 로직 구현:
▷ 오류 수정:
▷ 오류 부분:
'''

# 상어 이동
sdi = [-1, 0, 1, 0]
sdj = [0, -1, 0, 1]

# 물고기 이동
di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]


def fish_move(arr):
    nrr = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                ci, cj = i, j
                for fish in arr[i][j]:
                    d = fish
                    for _ in range(len(di)):
                        ni = ci + di[d]
                        nj = cj + dj[d]
                        if 0 <= ni < N and 0 <= nj < N and (ni, nj) != (si, sj) and smell[ni][nj] == 0:
                            nrr[ni][nj].append(d)
                            break
                        else:
                            d = (d - 1) % (len(di))
                    else:
                        nrr[i][j].append(fish)
    return nrr


def shark_move(smell, arr, si, sj):
    mx = -21e8
    pos = []
    for way in shark_dir:
        ci, cj = si, sj
        load = []
        for d in way:
            ni = ci + sdi[d]
            nj = cj + sdj[d]
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            load.append((ni, nj))
            ci, cj = ni, nj

        if len(load)==3:
            sset = set(load)
            cnt = 0
            for seti, setj in sset:
                cnt += len(arr[seti][setj])
            if mx < cnt:
                mx = cnt
                pos = way
    for d in pos:
        ni = si + sdi[d]
        nj = sj + sdj[d]
        if arr[ni][nj]:
            arr[ni][nj] = []
            smell[ni][nj] = 3
        si, sj = ni, nj
    return smell, arr, si, sj


def disappear_smell(smell):
    for i in range(N):
        for j in range(N):
            if smell[i][j]:
                smell[i][j] -= 1
    return smell


def magic(arr_copy, arr):
    for i in range(N):
        for j in range(N):
            if arr_copy[i][j]:
                for fish in arr_copy[i][j]:
                    arr[i][j].append(fish)
    return arr


N = 4
arr = [[[] for _ in range(N)] for _ in range(N)]
smell = [[0 for _ in range(N)] for _ in range(N)]
M, S = map(int, input().split())
for _ in range(M):
    x, y, d = map(int, input().split())
    x, y, d = x - 1, y - 1, d - 1
    arr[x][y].append(d)
si, sj = map(int, input().split())
si, sj = si - 1, sj - 1  # 상어 좌표
shark_dir = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            shark_dir.append((i, j, k))

for s in range(1, S + 1):
    arr_copy = [lst[:] for lst in arr]  # 1) 복사
    arr = fish_move(arr)  # 2) 이동
    smell, arr, si, sj = shark_move(smell, arr, si, sj)
    smell = disappear_smell(smell)
    arr = magic(arr_copy, arr)

    # print("///////", s, "회차//////////")
    # print("상어 위치:", si + 1, sj + 1)
    # print_fish(arr)
    # print("물고기냄새")
    # print2(smell)
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(arr[i][j])
print(ans)