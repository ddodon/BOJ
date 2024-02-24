'''
Memo 5567 결혼식
인접리스트 활용
결과 1) x
양방향 친구 추가 후 1만 삭제
결과 2) x
상근이랑만 친구인 경우 고려 못함
쉽게 풀려다 결국 더 걸림
'''

n = int(input())
m = int(input())
lst = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    lst[s].append(e)
    lst[e].append(s)
ans = set()
for i in lst[1]:
    ans.add(i)
    for j in lst[i]:
        if j!=1:
            ans.add(j)
print(len(ans))