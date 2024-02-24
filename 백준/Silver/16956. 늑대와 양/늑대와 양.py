'''
Memo 16956 늑대와 양
스페셜저지
탐색 후 다음좌표가 양의 위치면 현재 위치에 울타리 놓기
결과 1) 시간초과
BFS 없이, 양 주위에 전부 울타리 놓기로 변경
결과 2) x
*lst -> 공백있음...
'''

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
wolf = []
# 늑대 위치 확인 / 늑대 바로 옆에 양이면 즉시 종료
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'W':
            for k in range(len(di)):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 'S':
                    print(0)
                    exit()
# 양 위치 확인 / 4방에 울타리 두르기
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            for k in range(len(di)):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == '.':
                    arr[ni][nj] = 'D'
print(1)
for lst in arr:
    print("".join(lst))