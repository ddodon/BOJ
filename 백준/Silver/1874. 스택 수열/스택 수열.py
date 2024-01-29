N = int(input())
n = []
stk = []
ans = [] #답
tmp = 0
for _ in range(N):
    i = int(input())
    n.append(i)

for i in n:
    while tmp <= N+1:
        if stk and stk[-1] == i:
            stk.pop()
            ans.append('-')
            break
        else:
            tmp += 1
            stk.append(tmp)
            ans.append("+")
if len(stk) != 0:
    print("NO")
else:
    for i in range(len(ans)):
        print(ans[i])