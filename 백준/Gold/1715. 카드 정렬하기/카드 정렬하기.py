import sys
import heapq

input = sys.stdin.readline
N = int(input())
hq = []
res = 0
for i in range(N):
    x = int(input())
    heapq.heappush(hq,x)

for i in range(N-1):
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    heapq.heappush(hq,a+b)
    res += (a+b)
print(res)
