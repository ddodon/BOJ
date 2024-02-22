'''
Memo BOJ 3987 보이저 1호
무한대인 경우 -> 출발지로 돌아오고 첫 방향 그대로
사용자 정의 정렬(순서) 만드는 법 찾아보기
'''

# 최초방향: 시계
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def print_dir(ans):
    if ans == 0:
        print('U')
    elif ans == 1:
        print('R')
    elif ans == 2:
        print('D')
    elif ans == 3:
        print('L')


# 행성
def planet(i, j, k):
    if arr[i][j] == '\\':
        if k == 0:
            k = 3
        elif k == 1:
            k = 2
        elif k == 2:
            k = 1
        elif k == 3:
            k = 0
    elif arr[ni][nj] == '/':
        if k == 0:
            k = 1
        elif k == 1:
            k = 0
        elif k == 2:
            k = 3
        elif k == 3:
            k = 2
    return k


N, M = map(int, input().split())
arr = [['x' for _ in range(M + 2)]] + [['x'] + list(input()) + ['x'] for _ in range(N)] + [['x' for _ in range(M + 2)]]

# 최초 좌표 / 최초방향1(무한대 판별용) / 최초방향2
i, j = map(int, input().split())
pr, pc = i, j

# 방향별 배열
ans = [[0], [1], [2], [3]]

for k in (0, 1, 2, 3):
    first_dir = k
    flag = True
    cnt = 0  # 시간
    i, j = pr, pc
    while flag:
        ni = i + di[k]
        nj = j + dj[k]
        # 무한대 감지(다음 좌표가 출발지인데, 최초방향과 같음)
        if (ni, nj) == (pr, pc) and k == first_dir:
            cnt = -1000000
            flag = False
            break
        # 범위 밖 or 무한대
        elif arr[ni][nj] == 'x' or arr[ni][nj] == 'C':
            cnt += 1
            flag = False
            break
        # 빈 칸
        elif arr[ni][nj] == '.':
            cnt += 1
            i = ni
            j = nj
        # 행성
        elif arr[ni][nj] == '\\':
            cnt += 1
            i = ni
            j = nj
            k = planet(i, j, k)
        elif arr[ni][nj] == '/':
            cnt += 1
            i = ni
            j = nj
            k = planet(i, j, k)
    # 무한대
    if cnt == -1000000:
        print_dir(ans[first_dir][0])
        print('Voyager')
        exit()
    else:
        # 방향별 길이 추가
        ans[first_dir].append(cnt)
ans.sort(key=lambda x: (-x[1], x[0]))
print_dir(ans[0][0])
print(ans[0][1])