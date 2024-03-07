# 8방향
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def spring(loc):
    dead = []

    for i,j in loc:
        tlst = tree[i][j]
        tlst.sort()
        new_tree = []
        for t in range(len(tlst)):
            if feed[i][j] < tlst[t]:
                dead.append((i,j,tlst[t]))
            else:
                feed[i][j] -= tlst[t]
                tlst[t] += 1
                new_tree.append(tlst[t])
        tree[i][j] = new_tree
    return dead

def summer(dead):
    for d in range(len(dead)):
        i,j,f = dead[d]
        feed[i][j] += f//2

def autumn(loc):
    n_loc = set()
    if loc:
        for (i, j) in loc:
            for t in tree[i][j]:
                if t != 0 and t % 5 == 0:
                    for k in range(len(di)):
                        ni = i + di[k]
                        nj = j + dj[k]
                        if 0 <= ni < N and 0 <= nj < N:
                            tree[ni][nj].append(1)
                            n_loc.add((ni, nj))
    for (i,j) in n_loc:
        loc.add((i,j))

def winter():
    for i in range(N):
        for j in range(N):
            feed[i][j] += robot[i][j]

N, M, K = map(int, input().split())
robot = [list(map(int, input().split())) for _ in range(N)]
feed = [[5 for _ in range(N)] for _ in range(N)]
loc = set()
# dic = defaultdict(int)
tree = [[[] for _ in range(N)] for _ in range(N)]

# 나무 행/ 열 / 나무 나이
for _ in range(M):
    x, y, z = map(int, input().split())
    x, y = x - 1, y - 1
    loc.add((x,y))
    tree[x][y].append(z)
for _ in range(K):
    # 봄 / 여름 / 가을 / 겨울
    dead = spring(loc)
    summer(dead)
    autumn(loc)
    winter()

# for lst in tree:
#     print(lst)

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])
print(ans)