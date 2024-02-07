'''
Memo BOJ 13023
N명이 참가하는 알고리즘 캠프
0번 ~ N-1번까지의 참가자들 중 일부는 서로 친구사이
A - B, B - C, C  - D, D - E 와 같은 친구 관계가 있는지 구하기
adj배열 속 이어지는 관계가 5번
* 가능한 모든 경로 + 모든 node를 시작으로 경로를 탐색해야 풀 수 있는 문제
'''
# (i열 현재좌표, j열 현재좌표)
def dfs(cur,cnt):
    global ans
    # 중복방지
    #종료조건
    if cnt == 4:
        ans = 1
        return

    # 백트래킹 - adj속 배열이 이어지도록 하는 경우의 수가 존재한다면
    for n in adj[cur]:
        if v[n] == 0:
            v[n] = 1
            dfs(n, cnt+1)
            v[n] = 0

N, M = map(int,input().split())
adj=[[] for _ in range(N)]
v=[0]*N
# 이어지는 친구 사이
ans = 0

# 인접리스트 생성
for _ in range(M):
    s, e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

# adj 배열 정렬
for lst in adj:
    lst.sort()

# 모든 번호에서 탐색
for i in range(N):
    v[i] = 1
    dfs(i,0)
    v[i] = 0
    # 5관계 친구가 존재한다면
    if ans == 1:
        break
print(ans)