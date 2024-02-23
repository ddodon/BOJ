'''
Memo BOJ 20055 컨베이어 벨트 위의 로봇
1단계는 회전 (로봇이 있든 없든)
엣지) k가 1, 내구도 1
'''


def check_K(lst):  # 내구도 검사
    check = 0
    for i in range(len(lst)):
        if lst[i][1] <= 0:
            check += 1
    return check


def belt_move(lst):  # 벨트 이동
    lst.insert(0, lst.pop(-1))
    return lst


def robot_move(lst, cur):
    # 로봇 숫자, 내구도, 좌표
    for robot_number, a, idx in cur:
        if idx == 2 * N - 1:  # 마지막벨트 였다면
            if lst[0][0] == 0 and lst[0][1] > 0:
                lst[0][0] = robot_number
                lst[0][1] -= 1
                lst[idx][0] = 0
        else:
            if lst[idx + 1][0] == 0 and lst[idx + 1][1] > 0:
                lst[idx + 1][0] = robot_number
                lst[idx + 1][1] -= 1
                lst[idx][0] = 0
    return lst


def robot_cur(lst):  # 현재 로봇 좌표 (올린 순서대로)
    cur = []
    for i in range(len(lst)):
        if lst[i][0] > 0:
            cur.append((lst[i][0], lst[i][1], i))
    cur.sort(key=lambda x: (x[0]))
    return cur


def robot_start(lst):
    global robot
    if lst[0][0] == 0 and lst[0][1] > 0:
        lst[0][0] = robot
        lst[0][1] -= 1
        robot += 1
    return lst


def robot_out(lst):
    if lst[N - 1][0] > 0:
        lst[N - 1][0] = 0
    return lst


# 입력 / 벨트 이동방향대로 순서 변경 / [로봇유뮤 / 내구도]
N, K = map(int, input().split())
lst = [[0] for _ in range(2 * N)]
a = list(map(int, input().split()))
# a = a[:N]+a[N:][::-1]
for i in range(2 * N):
    lst[i].append(a.pop(0))

# 현재 진행 단계 / 로봇 번호
ans = 1
robot = 1

# 내구도가 0인 벨트가 K개 이상이면 종료
while 1:
    lst = belt_move(lst)  # 1.벨트 이동
    lst = robot_out(lst)

    cur = robot_cur(lst)  # 로봇 올린 순서 파악
    lst = robot_move(lst, cur)  # 2. 로봇 이동
    lst = robot_out(lst)
    lst = robot_start(lst)  # 3. 로봇적재

    if check_K(lst) >= K:  # 4. 내구도 검사
        break
    ans += 1
print(ans)