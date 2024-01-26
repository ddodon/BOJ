c, r = map(int,input().split())
square = 0
point_r = [] #가로 점선
point_c = [] #세로 점선
n = int(input())
if n < 1:
    print(r*c)
else:
    for i in range(n):
        d, point = map(int, input().split())
        if d == 0:
            point_r.append(point)
        else:
            point_c.append(point)
    point_r.append(0); point_c.append(0)
    point_r.append(r); point_c.append(c)
    point_r.sort(reverse=True);point_c.sort(reverse=True);
    row = 0; col = 0
    for i in range(len(point_r)-1):
        if row < point_r[i]-point_r[i+1]:
            row = point_r[i]-point_r[i+1]
    for i in range(len(point_c)-1):
        if col < point_c[i]-point_c[i+1]:
            col = point_c[i]-point_c[i+1]
    print(row*col)