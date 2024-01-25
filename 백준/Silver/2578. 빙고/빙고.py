def find_bingo(arr):
    gg = 0
    for i in range(5):
        if sum(arr[i][:]) == 5:#가로
            gg+=1
        if (arr[0][i]+arr[1][i]+arr[2][i]+arr[3][i]+arr[4][i]) == 5:#세로
            gg+=1
    if (arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3]+arr[4][4])==5:
        gg+=1
    if (arr[0][4]+arr[1][3]+arr[2][2]+arr[3][1]+arr[4][0])==5:
        gg+=1
    if gg >= 3:
        return True
    return False

res = 0
mc = []
bingo = [list(map(int,input().split())) for _ in range(5)]
b = [input().split() for _ in range(5)]
flag = [[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        mc.append(int(b[i][j]))

for k in range(12): #11개까진 빙고 없음
    find = False
    f = mc[k]
    for i in range(5):
        if find == True:
            break
        for j in range(5):
            if bingo[i][j] == f:
                flag[i][j] = 1
                find = True
                break
for k in range(12,25):
    if find_bingo(flag) == True:
        res = k
        break
    else:
        find = False
        f = mc[k]
        for i in range(5):
            if find == True:
                break
            for j in range(5):
                if bingo[i][j] == f:
                    flag[i][j] = 1
                    find = True
                    break
print(res)