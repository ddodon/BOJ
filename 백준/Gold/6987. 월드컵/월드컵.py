'''
BOJ 6987 월드컵
3^15번 모두 탐색하여 입력받은 케이스가 가능한지 판별 해야함
처음엔 갖가지 경우의 수를 대입하는 방식으로 풀었으나 무수한 반례들이 존재했음
'''

from itertools import combinations

def dfs(n):
    global ans
    #종료조건: 15경기 완료
    if n == 15:
        for r in res: # r = [승 무 패]
            if not (r[0]==r[1]==r[2]==0):
                ans = 0
                break
        else: # 승 무 패 모두 가능한 경우면 1
            ans = 1
        return
    # 백트래킹: 제 1경기부터 (승무패 숫자 하나씩 빼기)
    home, away = match[n]
    for i,j in ((0,2),(1,1),(2,0)):
        if res[home][i] > 0 and res[away][j]:
            res[home][i] -=1
            res[away][j] -=1
            dfs(n+1)
            res[home][i] +=1
            res[away][j] +=1

# 총 경기 수: 15경기 / 0~5국가 매치 경우의 수
match = list(combinations(range(6),2))
for _ in range(4):
    lst = list(map(int,input().split()))
    res = [lst[i:i+3] for i in range(0,16,3)]
    ans = 0
    dfs(0)
    print(ans,end=" ")