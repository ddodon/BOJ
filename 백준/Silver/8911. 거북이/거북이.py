'''
Memo BOJ 8911 거북이
최초 거북이의 위치는 0,0 / 북쪽
set에 이동할 때마다의 좌표 기록 후
각 축별 최대 이동범위 활용 직사각형 넓이 구하기
'''

# 시계방향
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    # 명령어 / 최초 거북이 방향 / 좌표 / 최초 좌표 set에 추가
    command = list(input())
    k = y = x = 0
    set_y = set()
    set_x = set()
    set_y.add(0)
    set_x.add(0)

    for c in command:
        # 전진
        if c == 'F':
            y = y + dy[k]
            x = x + dx[k]
            set_y.add(y)
            set_x.add(x)
        # 후진
        elif c == 'B':
            y = y - dy[k]
            x = x - dx[k]
            set_y.add(y)
            set_x.add(x)
        # 좌향좌
        elif c == 'L':
            k = (k - 1) % 4
        # 우향우
        else:
            k = (k + 1) % 4

    ans = abs(min(set_y) - max(set_y)) * abs(min(set_x) - max(set_x))
    print(ans)