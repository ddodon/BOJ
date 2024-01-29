# 방향 우상 우 우하 하
di = [0, 1, 1, -1]
dj = [1, 0, 1, 1]
table = [list(map(int, input().split())) for _ in range(19)]
ans = []
for i in range(19):
    for j in range(19):
        # 돌이 없으면
        if table[i][j] == 0:
            continue
        # 돌이 있으면
        else:
            stone = table[i][j]
            for k in range(4):
                omok = 1
                for t in range(1,5):  # 오목
                    ni = i + di[k]*t
                    nj = j + dj[k]*t
                    mi = i - di[k]
                    mj = j - dj[k]
                    if ni < 0 or nj < 0 or ni >= 19 or nj >= 19:
                        continue
                    if table[ni][nj] == stone:
                        omok += 1
                        if omok == 5:
                            #육목 체크
                            if mi >= 0 and mj >= 0 and mi < 19 and mj < 19 and table[mi][mj] == stone:
                                break
                            if ni+di[k] >= 0 and nj+dj[k] >= 0 and ni+di[k] < 19 and nj+dj[k] < 19 and table[ni+di[k]][nj+dj[k]] == stone:
                                break
                            ans.append(stone)
                            ans.append(i)
                            ans.append(j)
                            ans.append(k)
                    else:
                        break
if len(ans) == 0:
    print(0)
else:
    print(ans[0])
    print(ans[1]+1,ans[2]+1)