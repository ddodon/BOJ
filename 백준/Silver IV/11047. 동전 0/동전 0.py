N, K = map(int,input().split())
lst = []
for i in range(N):
    try:
        lst.append(int(input()))
    except:
        break
lst.sort(reverse=True)
cnt = 0
# 큰 금액부터 집어 넣기
for n in lst:
    cnt += K//n
    K = K%n
print(cnt)