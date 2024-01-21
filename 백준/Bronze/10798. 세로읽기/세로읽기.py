arr = []
mx_num = 0
for i in range(5):
    s = list(input())
    if len(s) > mx_num:
        mx_num = len(s)
    arr.append(s)

for i in range(mx_num):
    for j in range(5):
        try:
            print(arr[j][i],end="")
        except:
            pass