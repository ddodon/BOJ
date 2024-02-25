'''
Memo BOJ 1913 달팽이
중간부터 시작하려고 했으나 복잡할 것 같아서
N^2 숫자가 적힐 곳부터 내려오기 + 방문배열 [-1]로 둘러싸서 범위 조정 쉽게
* 실수한 부분: 최초 정답 좌표를 (0,0)으로 착각
'''

# 반시계 방향
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

N = int(input())
n = int(input())

# 방문체크 배열 -1로 둘러싸기
arr = [[-1] * (N + 2)] + [[-1] + [0 for _ in range(N)] + [-1] for _ in range(N)] + [[-1] * (N + 2)]

# 시작 좌표 / 최초 방향 / 정답 좌표
i = j = 1
k = 0
ans_i = ans_j = 1

# 삽입할 숫자
cnt = N ** 2
arr[i][j] = cnt

while cnt > 1:
    ni = i + di[k]
    nj = j + dj[k]

    if arr[ni][nj] == 0:
        cnt -= 1
        arr[ni][nj] = cnt
        if n == cnt:
            ans_i = ni
            ans_j = nj
        i = ni
        j = nj

    else:
        k = (k + 1) % 4

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(arr[i][j], end=" ")
    print()
print(ans_i, ans_j)