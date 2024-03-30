H,W = map(int,input().split())
h_cycle = [i for i in range(H+1)]+[i for i in range(H-1,0,-1)]
w_cylce = [i for i in range(W+1)]+[i for i in range(W-1,0,-1)]
x,y = map(int,input().split())
t = int(input())
print(h_cycle[(x+t)%len(h_cycle)],w_cylce[(y+t)%len(w_cylce)])