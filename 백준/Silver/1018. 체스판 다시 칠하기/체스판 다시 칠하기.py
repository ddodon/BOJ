# 8x8격자에서 새로 칠해야 하는 값 찾기
n, m = map(int, input().split())
chess = [input() for _ in range(n)]

# 8x8 완전탐색
mn = 32
w = b = 0
B = 'B'
W = 'W'
for _ in range(2):
    B, W = W, B
    for i in range(0, n - 7):
        for j in range(0, m - 7):
            w = b = c = 0
            for k in range(8):
                B, W = W, B
                # 2개의 경우의 수
                for t in range(0, 8, 2):
                    if chess[i + k][j:j + 8][t] != B:
                        w += 1
                    if chess[i + k][j:j + 8][t + 1] == B:
                        b += 1
            c = (w + b)
            if mn > c:  # 격자에서 새로 칠해야 하는 개수
                mn = c
print(mn)