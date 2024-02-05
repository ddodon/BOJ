S = list(map(str,input()))
bomb = list(map(str,input()))
str = []

for i in range(len(S)):
    str.append(S[i])
    if len(str) >= len(bomb) and str[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            str.pop(-1)
if str:
    print("".join(str))
else:
    print("FRULA")