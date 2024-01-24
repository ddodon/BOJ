h, w = map(int,input().split())
current_sky = [input() for _ in range(h)]
sky = [[-1]*w for _ in range(h)]

#시간별 구름 위치 삽입
for t in range(w):
    for i in range(h):
        for j in range(w):
            if current_sky[i][j] == 'c' and j+t < w:
                if sky[i][j+t] < 0: # 최소 구름 위치
                    sky[i][j+t] = t
for i in range(h):
    print(*sky[i])