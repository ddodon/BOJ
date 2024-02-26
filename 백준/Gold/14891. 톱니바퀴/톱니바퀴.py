'''
Memo BOJ 14891 톱니바퀴
left, right 인덱스 잘못 설정해서 시간 잡아먹음
'''


def turn(lst, clock):
    res = []
    if clock == 1:
        res = lst[:-1]
        res.insert(0, lst[-1])
        return res
    else:
        res = lst[1:]
        res.append(lst[0])
        return res


num = [0, 1, 2, 3]
# 입력: 2차원배열 [톱니번호][톱니]
lst = [[] for _ in range(4)]
for i in range(4):
    lst[i] = list(map(int, input()))

K = int(input())
for _ in range(K):
    n, d = map(int, input().split())
    if d == -1:
        d = 0
    k = n - 1  # 톱니 번호
    left, right = lst[k][6], lst[k][2]
    left_tmp, right_tmp = left, right
    d_tmp = d

    # 해당 톱니 회전
    lst[k] = turn(lst[k], d)

    for i in range(k, 0, -1):  # 왼쪽 톱니
        if lst[(i - 1) % 4][2] != left:  # 반대 회전
            d = (d + 1) % 2
            left, right = lst[(i - 1) % 4][6], lst[(i - 1) % 4][2]
            lst[(i - 1) % 4] = turn(lst[(i - 1) % 4], d)
        else:
            break

    d = d_tmp
    left, right = left_tmp, right_tmp
    for i in range(k, 4):  # 오른쪽 톱니
        if i + 1 >= 4:
            break
        if lst[(i + 1) % 4][6] != right:  # 반대 회전
            d = (d + 1) % 2
            left, right = lst[(i + 1) % 4][6], lst[(i + 1) % 4][2]
            lst[(i + 1) % 4] = turn(lst[(i + 1) % 4], d)
        else:
            break
ans = 0
for i in range(4):
    ans += lst[i][0] * (2 ** i)
print(ans)
