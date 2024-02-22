'''
Memo BOJ 13901 로봇
지정한 방향이 미리 입력됨
장애물이나 방문, 벽(범위 밖)을 만난 경우 방향 이동 (반복)
장애물이 없을 수도 있음
'''

# 기본방향(1234기준)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

R, C = map(int, input().split())
K = int(input())
arr = [[-1 for _ in range(C)] for _ in range(R)]

# 장애물 좌표
X = []
for _ in range(K):
    xi, xj = map(int, input().split())
    X.append((xi, xj))
    arr[xi][xj] = 'X'

# 시작좌표 / 이동길이
i, j = map(int, input().split())
arr[i][j] = 0
s = 0

# 설정방향 / 최초방향
dir = list(map(int, input().split()))
d = 0
k = dir[d] - 1

# 이동불가능 flag
flag = 0

# 이동
while flag < 4:
    ni = i + di[k]
    nj = j + dj[k]
    # 이동 가능: 범위 내 + 장애물x + 미방문
    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != 'X' and arr[ni][nj] < 0:
        s += 1
        arr[ni][nj] = s
        i = ni
        j = nj
        flag = 0
    # 방향 변경
    else:
        d = (d + 1) % 4
        k = dir[d] - 1
        flag += 1
# # 확인용
# for lst in arr:
#     print(lst)

print(i, j)