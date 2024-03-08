# dic -> 단순 for문 + 함수 리턴값/리스트 제거 실험
# set (1200ms)
# dic (시간초과)
di = [-1, -1, 0, 1, 1, 1, 0, -1]                    # 8방향
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def spring():
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                tree[i][j].sort()
                l = len(tree[i][j])
                for z in range(l):
                    if feed[i][j] < tree[i][j][z]:
                        for t in tree[i][j][z:l]:
                            newtree[i][j] += t // 2
                        tree[i][j] = tree[i][j][:z]
                        break
                    else:
                        feed[i][j] -= tree[i][j][z]
                        tree[i][j][z] += 1

def summer():
    for i in range(N):
        for j in range(N):
            feed[i][j] += newtree[i][j]


def autumn():
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                for z in tree[i][j]:
                    if z%5==0:
                        for k in range(len(di)):
                            ni = i + di[k]
                            nj = j + dj[k]
                            if 0 <= ni < N and 0 <= nj < N:
                                tree[ni][nj].append(1)

def winter():
    for i in range(N):
        for j in range(N):
            feed[i][j] += robot[i][j]

def cal():
    ans = 0
    for i in range(N):
        for j in range(N):
           ans += len(tree[i][j])
    return ans

N, M, K = map(int, input().split())             # 입력
robot = [list(map(int, input().split())) for _ in range(N)]
feed = [[5 for _ in range(N)] for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    x, y = x - 1, y - 1
    tree[x][y].append(z)

for _ in range(K):                              # 4계절
    newtree = [[0] * N for _ in range(N)]
    spring()
    summer()
    autumn()
    winter()
    
print(cal())                                    # 나무 개수