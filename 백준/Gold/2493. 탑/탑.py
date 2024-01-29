N = int(input())
tower = list(map(int,input().split()))
stk = []
ans = []
for i in range(N):
    while stk:
        if tower[i] > stk[-1][1]: # 타워가 더 높으면
            stk.pop() #이전 탑 의미 없음
        else:
            ans.append(stk[-1][0]+1)
            stk.append([i,tower[i]])
            break
    else:
        stk.append([i,tower[i]]) #인덱스 / 타워높이
        ans.append(0) #수신 불가
print(*ans)