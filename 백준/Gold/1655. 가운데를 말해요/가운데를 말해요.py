import sys
import heapq

def solution():
    left = [] #maxHeap
    right = []
    N = int(input())
    pivot = int(input())
    print(pivot)
    for flag in range(N-1):
        num = int(input())
        if num <= pivot:
            heapq.heappush(left,-num)
            if not (flag % 2):
                heapq.heappush(right, pivot)
                pivot = -heapq.heappop(left)

        else:
            heapq.heappush(right,num)
            if (flag%2):
                heapq.heappush(left,-pivot)
                pivot = heapq.heappop(right)

        # print(left, right)
        print(pivot)

if __name__=="__main__":
    input = sys.stdin.readline
    solution()