from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def find_default_dir():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                ai, aj = i, j
                for k in range(len(di)):
                    ni = ai + di[k]
                    nj = aj + dj[k]
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 3:
                        return (ai, aj, (k + 2) % 4, ni, nj, (k + 2) % 4)


def move_Ari(si, sj, d, HP_Ari):
    cnt = 0
    while cnt < 4:
        ni = si + di[d]
        nj = sj + dj[d]
        if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj] != 0:
            HP_Ari -= 1
            d = (d + 1) % 4
            cnt += 1
        else:
            break

    if cnt == 4: # 이동 불가
        return (si, sj, d, bi, bj, HP_Ari)

    else:
        arr[ni][nj] = 2
        arr[si][sj] = 0
    # 리턴: 다음위치,방향,직전위치
    return (ni, nj, d, si, sj, HP_Ari)


def snail(si, sj, d):
    # 총 확인할 칸 개수
    mx = N * M
    found = 1
    ci, cj = si, sj
    limit = 1
    step = 0
    flag = 0
    while 1:
        if (0 <= ci < N and 0 <= cj < M) and arr[ci][cj] == 1:  # 석순 찾음
            return (ci, cj)
            break
        if found == mx:  # 모든 칸 확인
            return False
            break
        ni = ci + di[d]
        nj = cj + dj[d]
        step += 1
        if step == limit:
            d = (d + 1) % 4
            flag += 1
            step = 0
            if flag == 2:
                flag = 0
                limit += 1
        if (0 <= ni < N and 0 <= nj < M):
            found += 1
        ci, cj = ni, nj


def monster(loc, hp):
    # 몬스터 소환 위치
    si, sj = loc
    q = deque()
    v = [[0] * M for _ in range(N)]
    v[si][sj] = 1
    q.append((si, sj, hp))

    while q:
        ci, cj, chp = q.popleft()
        if arr[ci][cj] == 2:
            return chp
        if chp == 0:
            return 0
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] != 3 and arr[ni][nj] != 1:
                q.append((ni, nj, chp - 1))
                v[ni][nj] = 1
    return 0


def check(HP_Ari, HP_Boss):
    if HP_Ari <= 0:
        print("CAVELIFE...")
        return True
    if HP_Boss <= 0:
        print("VICTORY!")
        return True
    return False

def pp():
    print("현재 아리체력",HP_Ari)
    print("현재 보스체력", HP_Boss)
    print2(arr)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
HP_Ari, Power_Ari, HP_Boss, Power_Boss = map(int, input().split())

# 0. 진행 방향 설정
ai, aj, dir_Ari, bi, bj, dir_Boss = find_default_dir()

while 1:
    # 1. 아리 공격
    HP_Boss -= Power_Ari
    # 체력검사
    if check(HP_Ari, HP_Boss):
        break
    # print("1. 아리공격")
    # pp()

    # 2. 아리 이동
    # 아리의 현재위치, 현재방향, 직전위치, 아리체력
    ai, aj, dir_Ari, pai, paj, HP_Ari = move_Ari(ai, aj, dir_Ari, HP_Ari)
    # print("2. 아리이동")
    # pp()


    # 체력검사
    if check(HP_Ari, HP_Boss):
        break

    # 3. 보스 공격 (몬스터 소환)
    res = snail(bi, bj, dir_Boss)
    if res:  # 3-1) 몬스터 소환 위치
        hit = monster(res, Power_Boss)
        HP_Ari -= hit
    #     print("몬스터가 있었고, 아리에게",hit,"공격")
    # print("3. 보스공격")
    # pp()


    # 체력검사
    if check(HP_Ari, HP_Boss):
        break

    # 4. 보스 이동
    arr[bi][bj] = 0
    arr[pai][paj] = 3
    bi,bj = pai,paj
    dir_Boss = dir_Ari
    # print("4. 보스이동")
    # pp()