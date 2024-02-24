'''
Memo 2447 별 찍기 10
9분할 별 찍기
dnc 부분 for문 안에 넣었다가 디버깅 오래걸림
실수*) 공백처리...
'''

def dnc(n, si, sj, blank):
    global arr
    # 종료조건
    if n == 1:
        if blank:
            arr[si][sj] = " "
        return

    # 정답조건
    if blank:
        for i in range(si, si + n):
            for j in range(sj, sj + n):
                arr[i][j] = " "
        return
    # 분할
    m = n // 3
    dnc(m, si, sj, 0)
    dnc(m, si, sj + m, 0)
    dnc(m, si, sj + (2 * m), 0)

    dnc(m, si + m, sj, 0)
    dnc(m, si + m, sj + m, 1)
    dnc(m, si + m, sj + (2 * m), 0)

    dnc(m, si + (2 * m), sj, 0)
    dnc(m, si + (2 * m), sj + m, 0)
    dnc(m, si + (2 * m), sj + (2 * m), 0)


N = int(input())
arr = [['*' for _ in range(N)] for _ in range(N)]

dnc(N, 0, 0, 0)

for lst in arr:
    print("".join(lst))