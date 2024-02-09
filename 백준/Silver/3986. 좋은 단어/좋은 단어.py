'''
Memo Boj 3986 좋은 단어
스택 활용
* 들어오는 값과 스택에 들어있던 값이 다를 때 추가하는 구문을 빼먹었다..
'''
from collections import deque

N = int(input())
arr = [list(input()) for _ in range(N)]
cnt = 0
for lst in arr:
    stk = deque()
    for i in range(len(lst)):
        if stk:
            if stk[-1] == lst[i]:
                stk.pop()
            else:
                stk.append(lst[i])
        else:
            stk.append(lst[i])
    if not stk:
        cnt += 1

print(cnt)