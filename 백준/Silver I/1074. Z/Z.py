'''
Memo BOJ 1074 Z
분할정복 문제
1 2 3 4 사분면 나눠서 생각하기   
'''


def dnc(r, c, n, ans):
    # 1. 종료조건
    if n == 0:
        print(ans)
        return

        # 2. 4분할 후 위치 파악
    m = 2 ** (n - 1)
    # 1) 1사분면
    if r < m and c < m:
        dnc(r, c, n - 1, ans)
    # 2) 2사분면
    elif r < m and c >= m:
        dnc(r, c - m, n - 1, ans + (m ** 2))
    # 3) 3사분면
    elif r >= m and c < m:
        dnc(r - m, c, n - 1, ans + (m ** 2) * 2)
    # 4) 4사분면
    elif r >= m and c >= m:
        dnc(r - m, c - m, n - 1, ans + (m ** 2) * 3)


N, r, c = map(int, input().split())
# 배열 속 숫자
ans = 0

# 분할정복
dnc(r, c, N, ans)