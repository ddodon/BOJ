n = int(input())
lst = [input() for _ in range(n)]
sorted_lst = list(set(sorted(lst,key=lambda x:(len(x),x))))
for i in range(len(sorted_lst)):
    print(sorted_lst[i])