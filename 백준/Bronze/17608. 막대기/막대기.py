n = int(input())
bar = []
for i in range(n):
    b = int(input())
    bar.append(b)
bar = bar[::-1] #오른쪽부터 시작
stk = []
for b in bar:
    if len(stk) == 0:
        stk.append(b)
    else:
        if b > stk[-1]: #더 큰 수가 들어와야 보임 (오른쪽에서)
            stk.append(b)
print(len(stk))