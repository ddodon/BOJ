'''
Memo BOJ 13567 로봇
명령은 범위 내에서만 유효 (시작 전 체크 후 유효하지 않으면 실행x)
로봇의 최초 방향은 동쪽
명령어열이 유효하지 않다면 -1
'''

# 방향 / 최초 방향(상우하좌) / 현재 좌표
di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]
k = 3
i = 0
j = 0

# 정사각형 변 길이 / 명령어 개수
M, N = map(int, input().split())

# 맵
arr = [[0 for _ in range(M)] for _ in range(M)]

# 명령어열
for _ in range(N):
    c, d = input().split()
    d = int(d)

    # 1) 이동
    if c == 'MOVE':
        ni = i + (di[k] * d)
        nj = j + (dj[k] * d)
        if not 0 <= ni <= M or not 0 <= nj <= M:
            print(-1)
            break
        else:
            i = ni
            j = nj

    # 2) 턴
    else:
        if d == 0:
            k = (k + 1) % 4
        else:
            k = (k - 1) % 4
# 이동완료
else:
    print(j, i)