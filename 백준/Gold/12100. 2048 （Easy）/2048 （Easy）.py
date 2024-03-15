# 총 시간: 58분
# 문제 읽기: 09:11 ~ 09:20
# 풀이 구상: 09:20 ~ 09:32
# 로직 구현: 09:32 ~ 09:51
# 오류 수정: 09:51 ~ 10:09
# 제출 결과: (1/2)
# 오류 부분: v배열을 통해 옮기면서 값이 바뀐 곳은 True 체크 해놨으나, 디버깅해보니 제대로 동작x
# (다음칸+현재칸도 체크했어야함)

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def dfs(n, tlst):                   # 4^5개의 순서를 모두 돌려보기 (가지치기는 일단 고려x)
    global ans
    if n == 5:
        arr = [lst[:] for lst in arr_o]
        for d in tlst:
            arr = game(arr, d)
        ans = max(max(map(max, arr)), ans)
        return
    for j in range(len(di)):
        dfs(n + 1, tlst + [j])

def game(arr, d):
    v = [[False] * N for _ in range(N)]
    if d < 2:                       # 위, 오른쪽 방향일 땐 (상단 우측부터 옮기기)
        for i in range(N):
            for j in range(N - 1, -1, -1):
                ci,cj = i,j
                while 1:
                    ni = ci + di[d]
                    nj = cj + dj[d]
                    if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == False and v[ci][cj] == False:
                        if arr[ni][nj] == 0:
                            arr[ni][nj] = arr[ci][cj]
                            arr[ci][cj] = 0
                            ci, cj = ni, nj
                        elif arr[ni][nj] == arr[ci][cj]:
                            arr[ni][nj] = arr[ci][cj] * 2
                            v[ni][nj] = True
                            arr[ci][cj] = 0
                            ci, cj = ni, nj
                        else: break
                    else: break

    else:                           # 아래, 왼쪽 방향일 땐 (하단 좌측부터 옮기기)
        for i in range(N - 1, -1, -1):
            for j in range(N):
                ci,cj = i,j
                while 1:
                    ni = ci + di[d]
                    nj = cj + dj[d]
                    if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == False and v[ci][cj] == False:
                        if arr[ni][nj] == 0:
                            arr[ni][nj] = arr[ci][cj]
                            arr[ci][cj] = 0
                            ci, cj = ni, nj
                        elif arr[ni][nj] == arr[ci][cj]:
                            arr[ni][nj] = arr[ci][cj] * 2
                            v[ni][nj] = True
                            arr[ci][cj] = 0
                            ci, cj = ni, nj
                        else: break
                    else: break
    return arr

N = int(input())
arr_o = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, [])
print(ans)