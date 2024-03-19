# 총 시간: 46분
# 문제 읽기: 8분
# 풀이 구상: 12분
# 로직 구현: 26분 (TC 완료)
# 오류 수정: 상어가 10,000 마리인 경우 (시간 초과 우려)
# 제출 결과: (1/1)
# 빨리 풀었으나, 10,000인 경우에 대한 처리 방법을 고민 (나머지 연산을 통해 다음 좌표를 정하는 부분에서 연산을 줄일 수 있을 것 같아 시도해봄)
# 시도해보다가 조금 꼬여서 일단 처음 만들어둔 로직을 output.txt에 10000개 케이스 출력해보고 돌아가길래 제출 + 성공
# 그러나, 시간이 2910ms로 느린 편
# 리팩토링
# 다음 위치 계산 함수 생성 → 상어가 움직이는 cycle (행의 경우 2R-2)
# cycle 내, 상어를 0에서 출발한다고 가정 + 기존 위치 + speed -> 다음 좌표

di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]
opp = {0: 1, 1: 0, 2: 3, 3: 2}


def return_shark_size(j):
    for i in range(R):
        if arr[i][j]:  # 상어가 있으면
            size = arr[i][j][2]
            arr[i][j] = []
            return size
    return 0


def move(arr):
    nrr = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j]:  # 상어가 있으면, 이동
                ni, nj, nd = next_loc(i, j, arr[i][j][0], arr[i][j][1]) # 좌표 / speed / 방향
                if not nrr[ni][nj] or (nrr[ni][nj][2] < arr[i][j][2]):
                    nrr[ni][nj] = [arr[i][j][0], nd, arr[i][j][2]]
    return nrr

def next_loc(i, j, speed, dir):
    if dir == UP or dir == DOWN:
        cycle = R * 2 - 2
        if dir == UP:
            speed += cycle - i
        else:
            speed += i
        speed %= cycle
        if speed >= R:
            return (cycle - speed, j, UP)
        return (speed, j, DOWN)
    else:
        cycle = C * 2 - 2
        if dir == LEFT:
            speed += cycle - j
        else:
            speed += j
        speed %= cycle
        if speed >= C:
            return (i, cycle - speed, LEFT)
        return (i, speed, RIGHT)


UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3
R, C, M = map(int, input().split())
arr = [[[] for _ in range(C)] for _ in range(R)]
ans = 0

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r, c, d = r - 1, c - 1, d - 1
    arr[r][c] = [s, d, z]

for j in range(C):
    ans += return_shark_size(j)  # 상어 잡기
    arr = move(arr)  # 상어 이동
print(ans)
