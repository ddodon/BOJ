mn, mx = map(int, input().split())
lst = [1] * (mx - mn + 1)
for i in range(2, int(mx ** 0.5) + 1):  # 소수판별
    pow = i ** 2  # 제곱수
    for j in range(int(mn //pow * pow), mx + 1, pow):
        if j - mn >= 0 and lst[j - mn] == 1:
            lst[j - mn] = 0
print(sum(lst))