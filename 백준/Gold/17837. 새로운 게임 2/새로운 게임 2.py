
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
opp = {0: 1, 1: 0, 2: 3, 3: 2}
White,Red,Blue = 0,1,2

def move():
    # 1번말부터
    for horse in range(1,K+1):
        ci,cj,cd = horse_info[horse]
        horse_idx = arr[ci][cj].index(horse)
        # 1. 이동 (다음 칸 확인)
        ni = ci + di[cd]
        nj = cj + dj[cd]
        # 1-1. 다음 칸이 범위 밖 or 파란칸이면 반대 이동
        if not (0<=ni<N and 0<=nj<N) or color[ni][nj] == Blue:
            cd = opp[cd]
            ni = ci + di[cd]
            nj = cj + dj[cd]
            if not (0 <= ni < N and 0 <= nj < N) or color[ni][nj] == Blue:
                horse_info[horse] = [ci, cj, cd]
                continue
            elif color[ni][nj] == White:
                for h in range(horse_idx, len(arr[ci][cj])):
                    arr[ni][nj].append(arr[ci][cj][h])
                    if arr[ci][cj][h]==horse:
                        horse_info[arr[ci][cj][h]][2] = cd
                    horse_info[arr[ci][cj][h]][0],horse_info[arr[ci][cj][h]][1] = ni,nj
            else:
                for h in range(len(arr[ci][cj])-1,horse_idx-1, -1):
                    arr[ni][nj].append(arr[ci][cj][h])
                    if arr[ci][cj][h]==horse:
                        horse_info[arr[ci][cj][h]][2] = cd
                    horse_info[arr[ci][cj][h]][0],horse_info[arr[ci][cj][h]][1] = ni,nj

        # 1-2. 흰색 칸이면
        elif color[ni][nj] == White:
            for h in range(horse_idx, len(arr[ci][cj])):
                arr[ni][nj].append(arr[ci][cj][h])
                horse_info[arr[ci][cj][h]][0],horse_info[arr[ci][cj][h]][1] = ni,nj

        # 1-3. 빨간 칸이면
        else:
            for h in range(len(arr[ci][cj]) - 1, horse_idx - 1, -1):
                arr[ni][nj].append(arr[ci][cj][h])
                horse_info[arr[ci][cj][h]][0],horse_info[arr[ci][cj][h]][1] = ni,nj
        arr[ci][cj] = arr[ci][cj][:horse_idx]

        # 2. 말 4개 쌓였는지 검사
        if arr[ci][cj] and len(arr[ci][cj]) > 3:
            return True
        elif arr[ni][nj] and len(arr[ni][nj]) > 3:
            return True
    return False

N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]
arr = [[[] for _ in range(N)] for _ in range(N)]
horse_info = [[0]]
for k in range(1, K + 1):
    x, y, d = map(int, input().split())
    x, y, d = x - 1, y - 1, d - 1
    horse_info.append([x,y,d])
    arr[x][y].append(k)
for t in range(1, 1001):
    # 1. 말의 이동 (순서대로)
    flag = move()
    if flag:
        print(t)
        break
else:
    print(-1)