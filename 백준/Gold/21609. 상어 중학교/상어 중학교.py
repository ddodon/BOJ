# 총 시간: 분
# 문제 읽기:  ~
# 풀이 구상:  ~
# 로직 구현: 10:09 ~
# 오류 수정:  ~
# 제출 결과: (/3)
# 오류 부분: 전부 0인경우, 무지개블럭은 매번 포함했어야 함

from collections import defaultdict, deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(i, j, block, num):
    q = deque()
    q.append((i, j))
    block = block
    rainbow = []
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                if (arr[ni][nj] == block or arr[ni][nj] == 0):
                    if arr[ni][nj] == 0:
                        rainbow.append((ni,nj))
                    v[ni][nj] = num
                    q.append((ni, nj))
                    cnt += 1
    if cnt > 1:
        dic[(i, j)] = [cnt]
        if rainbow:
            dic[(i, j)].append(len(rainbow))
        else:
            dic[(i, j)].append(0)

    for ri,rj in rainbow:
        v[ri][rj] = 0


def shark(i,j,num):
    q = deque()
    v = [[0]*N for _ in range(N)]
    q.append((i,j))
    v[i][j] = 0
    arr[i][j] = -2

    while q:
        ci,cj = q.popleft()
        for k in range(len(di)):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                if (arr[ni][nj] == num or arr[ni][nj] == 0):
                    arr[ni][nj]=-2
                    q.append((ni,nj))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0

def gravity(arr):
    d = 2
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            si, sj = i, j
            if arr[i][j] > -1:
                while 1:
                    ni = i + di[d]
                    nj = j + dj[d]
                    if (0 <= ni < N and 0 <= nj < N and arr[ni][nj] == -2):
                        arr[ni][nj] = arr[i][j]
                        arr[i][j] = -2
                    else:
                        i, j = si, sj
                        break
                    i, j = ni, nj
    return arr

while 1:
    num = 1
    dic = defaultdict(list)
    v = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0 and arr[i][j] > 0:
                v[i][j] = num
                bfs(i, j, arr[i][j], num)
                num += 1
    lst = sorted([(v, k) for k, v in dic.items()], key=lambda x: (-x[0][0], -x[0][1], -x[1][0], -x[1][1]))
    if not lst: break
    for point, (si, sj) in lst:
        if arr[si][sj] > 0:
            break
        else:
            continue
    if point[0] == 1:
        break
    ans += (point[0]) ** 2
    shark(si,sj,arr[si][sj])

    arr = gravity(arr)
    arr = [list(lst) for lst in zip(*arr)][::-1]
    arr = gravity(arr)
print(ans)