'''
Memo BOJ 2529 부등호
*실수한 포인트 (리스트 안에 숫자가 있으면 join 안먹힌다)
'''

def dfs(n):
    global ans
    # 정답조건: 숫자 선택 이후 부등후 붙여넣고 비교 (K>=2)
    if n >= 2:
        for i in range(len(ans) - 1):
            # 뒤 수가 더 작으면 back
            if lst[i] == '<' and ans[i] >= ans[i + 1]:
                return
            if lst[i] == '>' and ans[i] <= ans[i + 1]:
                return

    # 종료조건: K+1개 숫자 선택
    if n == K + 1:
        # 실수한 포인트 (리스트 안에 숫자가 있으면 join 안먹힌다)
        res.append("".join(str(s) for s in ans))
        return

    # 백트래킹
    for j in range(10):
        if v[j] == 0:
            v[j] = 1
            ans.append(j)
            dfs(n + 1)
            v[j] = 0
            ans.pop()

K = int(input())
lst = list(input().split())

ans = []
res = []
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
v = [0 for _ in range(10)]
dfs(0)
print(res[-1],res[0],sep='\n')