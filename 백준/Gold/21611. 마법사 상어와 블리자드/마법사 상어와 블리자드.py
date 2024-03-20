'''
Memo Boj 21611 마법사 상어와 블리자드 
메모리: 
시간: 
결과: 1/4 
풀이시간: 108분
▷ 문제 읽기: 15분
▷ 풀이 구상: 17분
▷ 로직 구현: 30분
    - 달팽이 순서 구슬 땡겨오기 (빈칸 2개 겹치니 하나만 채워짐) (55분)
    - 달팽이 로직을 한번만 사용하면 될 것 같은데, 방법을 모르겠어서 동작마다 하드코딩
▷ 오류 수정: 5분 + 5분
▷ 오류 부분: 블리자드 마법시 범위 실수 0<=nj<N -> 0<nj<N, 폭발 시 가지치기 괜히 해서 모두 같은 구슬일 때 안터짐
▷ 기타: 문제 정독 2회, 달팽이 순서 완성 6분
'''

# 달팽이 방향
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

# 마법 방향
mi = [0, -1, 1, 0, 0]
mj = [0, 0, 0, -1, 1]

# 구슬 땡기기
def nail(arr,si,sj):
    nail_arr = [[0] * N for _ in range(N)]
    lst = []
    ci, cj = si, sj
    limit = 1
    step = 0
    turn_flag = 0
    d = 0
    while 1:
        ni = ci + di[d]
        nj = cj + dj[d]
        if not (0 <= ni < N and 0 <= nj < N): break
        if arr[ni][nj]:
            lst.append(arr[ni][nj])
        step += 1
        if step == limit:
            turn_flag += 1
            if turn_flag % 2 == 0:
                limit += 1
            step = 0
            d = (d + 1) % 4
        ci, cj = ni, nj
    ci, cj = si, sj
    limit = 1
    step = 0
    turn_flag = 0
    d = 0
    for num in lst:
        ni = ci + di[d]
        nj = cj + dj[d]
        if not (0 <= ni < N and 0 <= nj < N): break
        nail_arr[ni][nj]=num
        step += 1
        if step == limit:
            turn_flag += 1
            if turn_flag % 2 == 0:
                limit += 1
            step = 0
            d = (d + 1) % 4
        ci, cj = ni, nj
    return nail_arr

def explosion(arr):
    ci, cj = si, sj
    limit = 1
    step = 0
    turn_flag = 0
    d = 0
    group = []
    flag = False
    while 1:
        ni = ci + di[d]
        nj = cj + dj[d]
        if not (0 <= ni < N and 0 <= nj < N): break
        if not group or arr[group[-1][0]][group[-1][1]]==arr[ni][nj]:
            group.append((ni,nj))
        else:
            if len(group)>=4:
                idx = arr[group[-1][0]][group[-1][1]]
                flag = True
                for gi,gj in group:
                    arr[gi][gj] = 0
                    ans[idx]+=1
            group = [(ni,nj)]
        step += 1
        if step == limit:
            turn_flag += 1
            if turn_flag % 2 == 0:
                limit += 1
            step = 0
            d = (d + 1) % 4
        ci, cj = ni, nj
    return (arr,flag)


def new(arr):
    nail_arr = [[0] * N for _ in range(N)]
    ci, cj = si, sj
    limit = 1
    step = 0
    turn_flag = 0
    d = 0
    group = []
    lst = []
    while 1:
        ni = ci + di[d]
        nj = cj + dj[d]
        if not (0 <= ni < N and 0 <= nj < N): break
        if not group or arr[group[-1][0]][group[-1][1]] == arr[ni][nj]:
            group.append((ni, nj))
        else:
            idx = arr[group[-1][0]][group[-1][1]]
            lst.append(len(group))
            lst.append(idx)
            group = [(ni, nj)]
        step += 1
        if step == limit:
            turn_flag += 1
            if turn_flag % 2 == 0:
                limit += 1
            step = 0
            d = (d + 1) % 4
        ci, cj = ni, nj
    ci, cj = si, sj
    limit = 1
    step = 0
    turn_flag = 0
    d = 0
    for num in lst:
        ni = ci + di[d]
        nj = cj + dj[d]
        if not (0 <= ni < N and 0 <= nj < N): break
        nail_arr[ni][nj]=num
        step += 1
        if step == limit:
            turn_flag += 1
            if turn_flag % 2 == 0:
                limit += 1
            step = 0
            d = (d + 1) % 4
        ci, cj = ni, nj
    return nail_arr




N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
si, sj = N // 2, N // 2
ans = [0]*4                        # 0. 구슬 별 정답
for _ in range(M):
    magic_d, magic_s = map(int, input().split())    # 1. 블리자드
    for k in range(1, magic_s + 1):
        ni = si + (mi[magic_d] * k)
        nj = sj + (mj[magic_d] * k)
        if 0<=ni<N and 0<=nj<N:
            arr[ni][nj]=0
    while 1:
        arr = nail(arr,si,sj)
        arr,flag = explosion(arr)
        if not flag: break
    arr = new(arr)
print(ans[1]+(ans[2]*2)+ans[3]*3)