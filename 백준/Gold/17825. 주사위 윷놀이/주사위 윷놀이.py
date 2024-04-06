# 칸 별 점수
point = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40,\
         13, 16, 19, 25, 30, 35, 22, 24,28, 27, 26, 0]
loc = [[1],[2],[3],[4],[5],[6,21],[7],[8],[9],[10],[11,27],[12],[13],[14],[15],[16,29],[17],[18],[19],[20],[32],\
       [22],[23],[24],[25],[26],[20],[28],[24],[30],[31],[24],[32],[32],[32],[32],[32]]

def dfs(n,sm):
    global ans
    # 종료조건: 주사위 10회 던지기
    if n==10:
        ans = max(ans,sm)
        return

    # 말 4개
    for j in range(4):
        horse = now[j]
        nx_loc = loc[horse][-1] # 1칸 전진하는 경우
        for _ in range(1,lst[n]):
            nx_loc = loc[nx_loc][0] # 나머진 칸 전진

        if nx_loc==32 or nx_loc not in now:
            now[j] = nx_loc
            dfs(n+1,sm+point[nx_loc])
            now[j]=horse

lst = list(map(int, input().split()))
ans = 0
now = [0,0,0,0]
dfs(0,0)
print(ans)