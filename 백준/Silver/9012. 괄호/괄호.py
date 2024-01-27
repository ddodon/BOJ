lst = []
n = int(input())
for i in range(n):
    s = input()
    check = 'NO'
    vps = 0
    for j in range(len(s)):
        #시작값
        if s[j] == '(':
            vps += 1
        else:
            if vps > 0:
                vps -= 1
            else:
                check = 'NO'
                vps += 1
                break
    if vps == 0:
        check = 'YES'
    print(check)