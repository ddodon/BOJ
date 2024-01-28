n = int(input())
for i in range(n):
    lst = []
    for j in range(len(str(i))):
        lst.append(int(str(i)[j]))

    if i + sum(lst) == n:
        print(i)
        break
else:
    print(0)