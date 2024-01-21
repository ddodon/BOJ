h, m = map(int,input().split())
minute = h*60+m-45
print(23 if minute//60 < 0 else minute//60 , minute%60)