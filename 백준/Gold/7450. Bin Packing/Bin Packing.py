import sys

#sys.stdin = open("input7450.txt","r")


n = int(input())
w = int(input())
items = [0] * n
for i in range(n):
    items[i] = int(input())

items=sorted(items)

start = 0
end = n-2
cnt = 0
#print(items,start,end)

while (start <= end):
    if(items[start] + items[end] <= w):
        start += 1
    end -= 1
    cnt += 1
print(cnt+1)  