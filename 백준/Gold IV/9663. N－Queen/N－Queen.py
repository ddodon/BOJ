# memo
# 가로 세로 대각별 배열을 구성한다까진 생각이 닿았지만
# 좌표를 어떻게 넘겨줄까에서 오래 막힘
# 각 배열 모두가 0이 가능한 조합찾기

def dfs(n):
    global ans
    # 정답조건: 퀸을 N개 놓았을 때
    if n == N:
        ans += 1
        return
    # 퀸 놓기
    for q in range(N):
        # 퀸을 놓을 수 있는 범위
        if row[q] == 0 and col[q] == 0 and diag_1[n+q] == 0 and diag_2[n-q] == 0:
            row[q] = 1
            col[q] = 1
            diag_1[n+q] = 1
            diag_2[n-q] = 1

            dfs(n + 1)

            # 원상복구
            row[q] = 0
            col[q] = 0
            diag_1[n+q] = 0
            diag_2[n-q] = 0


# 체스판 / 좌표 배열 생성
N = int(input())
arr = [[0] * (N) for _ in range(N)]

# 행 / 열 / 대각선의 개수1 (i+j) / 대각선의 개수2 abs(i-j)
row = [0] * (N)
col = [0] * (N)
diag_1 = [0] * (2*N-1)
diag_2 = [0] * (2*N-1) #파이썬 -1 배열 활용가능

# 퀸을 놓은 방법의 수
ans = 0
# 백트래킹 (n)
dfs(0)
print(ans)