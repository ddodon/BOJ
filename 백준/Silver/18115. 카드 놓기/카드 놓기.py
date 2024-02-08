'''
Memo Boj 18115 그림
덱 사용으로 시간초과 해결, 역 순서로 덱에 끼워넣기
'''
from collections import deque
N = int(input())
lst = list(map(int,input().split()))
ans = deque()
for i in range(1,N+1):
    a = lst.pop(-1)
    if a == 1:
        ans.insert(0,i)
    elif a == 2:
        ans.insert(1, i)
    else:
        ans.append(i)
print(*ans)