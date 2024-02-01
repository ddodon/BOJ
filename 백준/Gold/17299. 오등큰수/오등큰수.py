N = int(input())
lst = list(map(int,input().split()))
stk = []
ans = [-1 for _ in range(N)]

freq = [0 for _ in range(1000_001)]

for i in lst:
    freq[i] += 1 #lst배열 속 빈도만큼 등록

for i in range(N-1,-1,-1):
    while stk and freq[lst[i]] >= freq[stk[-1]]: #오등큰수 조건
        stk.pop()
    if stk:
        ans[i] = stk[-1]
    stk.append(lst[i])
print(*ans)
