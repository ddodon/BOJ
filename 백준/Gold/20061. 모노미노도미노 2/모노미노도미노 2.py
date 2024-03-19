
'''
Memo Boj 20061 모노미노도미노2
메모리: 119184 KB
시간: 612 ms
결과: (1/3)
풀이시간: 분 
▷ 문제 읽기: 분
▷ 풀이 구상: 분
▷ 로직 구현: 분
▷ 오류 수정: @분
▷ 오류 부분: 정답 제출 위한 코드에서 방향 좌표 빼먹음 + 한줄 완성 시 터지고 움직일 때 처음부터 움직이게 설계함
    (풀이 시작 90분 / 잠깐 휴식)
리팩토링 버전
'''

def gravity(arr, t, line):  # line: 행 or 열
    if t == 1:              # 1x1 도미노 중력
        for i in range(B):
            if arr[i][line] == 1:
                arr[i - 1][line] = 1
                break
        else:
            arr[B - 1][line] = 1

    elif t == 2:            # 1x2 도미노 중력
        for i in range(B):
            if arr[i][line] == 1 or arr[i][line + 1] == 1:
                arr[i - 1][line] = arr[i - 1][line + 1] = 1
                break
        else:
            arr[B - 1][line] = arr[B - 1][line + 1] = 1

    elif t == 3:            # 2x1 도미노 중력
        for i in range(B):
            if arr[i][line] == 1:
                arr[i - 1][line] = arr[i - 2][line] = 1
                break
        else:
            arr[B - 1][line] = arr[B - 2][line] = 1
    return arr

def bubble(arr):
    global ans
    for i in range(B):      # 한 줄 완성 시 버블
        if arr[i].count(1) >= 4:
            arr.pop(i)
            arr.insert(0,[0]*A)
            ans += 1
    for _ in range(2):      # 연한 칸에 도미노 있으면 버블
        if arr[1].count(1) >= 1:
            arr.pop(B-1)
            arr.insert(0, [0] * A)
    return arr

N = int(input())
A, B = 4, 6
green = [[0] * A for _ in range(B)]
blue = [[0] * A for _ in range(B)]
blue_table = {1: 1, 2: 3, 3: 2}  # 파란색은 2-3번 도미노가 반대
ans = 0
for _ in range(N):
    t, x, y = map(int, input().split())

    green = gravity(green, t, y)
    blue = gravity(blue, blue_table[t], x)

    green = bubble(green)
    blue = bubble(blue)

print(ans)  # 총 점수
sm_blue = sum(map(sum, blue))
sm_green = sum(map(sum, green))
print(sm_blue + sm_green)  # 총 블럭 개수