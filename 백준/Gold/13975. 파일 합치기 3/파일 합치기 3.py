import sys
import heapq

def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        hq = list(map(int,input().split()))
        heapq.heapify(hq)
        res = 0
        for _ in range(N - 1):
            a = heapq.heappop(hq)
            b = heapq.heappop(hq)
            heapq.heappush(hq, a + b)
            res += (a + b)
        print(res)

if __name__=="__main__":
    input = sys.stdin.readline
    solution()