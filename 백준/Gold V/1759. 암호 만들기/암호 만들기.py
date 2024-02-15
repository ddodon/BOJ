'''
Memo 1759 암호 만들기
백트래킹 문제
모음은 하나만, 자음은 최소 2개
암호는 사전순 오름차순 정렬된 형태
*실수) 인덱스 번호 설정 26번줄 -> 그냥 idx+1로 했었음
'''


def dfs(n, idx):
    # 종료조건
    if n == L:
        # 자/모음 체크
        cnt = 0
        for i in a_lst:
            if i in ans:
                cnt += 1
        # 모음 개수 1개 이상 + 자음 개수 2개 이상이면 추가
        if cnt >= 1 and len(ans) - cnt >= 2:
            print("".join(ans))
        return

    # 백트래킹
    for j in range(idx, C):
        ans.append(lst[j])
        dfs(n + 1, j + 1)
        ans.pop()


L, C = map(int, input().split())
lst = list(input().split())
v = [0 for _ in range(C)]
a_lst = ['a', 'e', 'i', 'o', 'u']

# 사전순 정렬
lst.sort()
ans = []
dfs(0, 0)