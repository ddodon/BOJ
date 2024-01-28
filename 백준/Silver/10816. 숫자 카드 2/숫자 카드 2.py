n = int(input())
dic = {}
lst_n = list(map(int,input().split()))

m = int(input())
lst_m = list(map(int,input().split()))

for i in range(n):
    if lst_n[i] not in dic:
        dic[lst_n[i]] = 1
    else:
        dic[lst_n[i]] += 1

for i in range(m):
    if lst_m[i] in dic:
        print(dic[lst_m[i]], end=" ")
    else:
        print(0, end=" ")