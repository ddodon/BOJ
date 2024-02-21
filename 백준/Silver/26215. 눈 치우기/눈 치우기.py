'''
Memo BOJ 26215 눈치우기
첫번째 값을 메울 수 있는 만큼 뒤 리스트에서 찾음
엣지) 10 10 3 1 1 1 1
*실수한 부분) import sys open부분까지 복사해버림 + 제출 전에 확인하는 습관 가지기
** 처음풀이) 치울 때마다 리스트에서 pop시켰고, 엣지케이스를 찾지못함
*** 정렬을 매번 함
'''

# 입력
N = int(input())
lst = list(map(int, input().split()))

cnt = 0
if N >= 2:
    # 집이 2개 이상 있는 경우
    for _ in range(N):
        lst.sort(reverse=True)
        lst[0] -= lst[1]
        cnt += lst[1]
        lst[1] = 0

# 집이 하나 남은 경우
cnt += sum(lst)
if cnt > 1440:
    print(-1)
else:
    print(cnt)
