import heapq
import sys

input = sys.stdin.readline
N = int(input())
hq = []
for i in range(N):
    x = int(input())
    if x == 0:
        try:
            print(heapq.heappop(hq)[1])
        except:
            print(0)
    else:
        heapq.heappush(hq, (abs(x),x))
