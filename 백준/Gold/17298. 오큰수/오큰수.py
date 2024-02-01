N = int(input())
lst = list(map(int,input().split()))
ans = [0 for _ in range(N)]
stk = []

for i in range(N):
    while stk and lst[stk[-1]]< lst[i]: #오큰수가 되는 조건
        ans[stk[-1]] = lst[i]
        stk.pop()
    stk.append(i) # 인덱스를 스택에 저장 ㅠ..ㅠ
while stk:
    ans[stk[-1]] = -1 #스택에 남은 숫자 -1처리
    stk.pop()
print(*ans)