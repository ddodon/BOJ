N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
ans = 21e8
for a in range(N-2):
    for b in range(1, N - 1):
        for cc in range(1, N):
            for dd in range(1, N):
                gu = [0,0,0,0,0,0]
                x, y, d1, d2 = a, b, cc, dd
                if a + cc + dd > N: continue
                if b + dd > N: continue
                if b - cc < 1: continue
                arr = [[5] * N for _ in range(N)]
                for i in range(d1 + 1):
                    for j in range(d2 + 1):
                        # 1구역
                        for r in range(x + i):
                            for c in range(y - i + 1):
                                arr[r][c] = 1
                        # 2구역
                        for r in range(x + j + 1):
                            for c in range(y + j + 1, N):
                                arr[r][c] = 2
                        # 3구역
                        for r in range(x + d1 + j, N):
                            for c in range(y - d1 + j):
                                arr[r][c] = 3
                        # 4구역
                        for r in range(x + d2 + i+1, N):
                            for c in range(y + d2 - i, N):
                                arr[r][c] = 4
                for o in range(N):
                    for p in range(N):
                        gu[arr[o][p]] += people[o][p]
                if gu.count(0)>1:
                    continue
                res = max(gu[1:]) - min(gu[1:])
                ans = min(ans, res)
print(ans)