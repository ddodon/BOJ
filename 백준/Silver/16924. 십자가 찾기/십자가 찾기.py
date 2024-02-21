'''
Memo BOJ 16924 십자가 찾기
사용할 수 있는 십자가는 N*M개 이하
같은 위치라면 십자가 길이가 긴 것부터 출력
*실수) 어떻게든 N*M개 이하의 십자가로 채울 수 있다면 가능하다고 보는 듯
**다 지우고 다시) N*M개 이하의 최소 개수로 구할 경우만 탐색 + 가장 긴 십자가부터
'''

# 시계방향
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 입력
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
v = [[0 for _ in range(M)] for _ in range(N)]

# 기본 십자가 최대길이 / 십자가배열
T = (min(N, M) // 2)
ans = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == '*':
            mx_t = 0
            flag = 0
            for t in range(1, T + 1):
                if flag:
                    break
                cnt = 0
                for k in range(len(di)):
                    ni = i + (di[k] * t)
                    nj = j + (dj[k] * t)
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '*':
                        cnt += 1
                    else:
                        flag = 1
                        break
                if cnt == 4:
                    mx_t = t
            if mx_t>0:
                ans.append([i, j, mx_t])
                v[i][j] = 1
                for l in range(1, mx_t + 1):
                    for kk in range(len(di)):
                        li = i + (di[kk] * l)
                        lj = j + (dj[kk] * l)
                        v[li][lj] = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == '*' and v[i][j] == 0:
            print(-1)
            exit(0)
print(len(ans))
for i, j, t in ans:
    print(i + 1, j + 1, t)