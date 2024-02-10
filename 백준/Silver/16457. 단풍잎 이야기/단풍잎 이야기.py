'''
Memo BOJ 16457 단풍잎 이야기
백트래킹으로 최대 퀘스트 클리어 숫자 구하기
'''
# 선택 횟수 / 인덱스
def dfs(n,s):
    global ans
    if n == N:
        tmp = 0
        for keys in arr:
            for key in keys:
                if key not in v:
                    break
            else:
                tmp += 1
        ans = max(tmp,ans)
    for i in range(s,N*2):
        if v[i] == 0:
            v[i] = i+1
            dfs(n+1,i+1)
            v[i] = 0

# 남은 키, 퀘스트 수, 스킬 개수
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
# 퀘스트에 필요한 키 모음
v = [0]*(2*N)
ans = 0
dfs(0,0)
print(ans)
