N = int(input())
time = []
ans = 0
for _ in range(N):
    s, e = map(int, input().split())
    time.append((s, e))

# 회의 시작하자마자 끝난 경우가 있으므로 추가 정렬
time.sort(key=lambda x: (x[1],x[0]))

# 마지막에 끝난 시간
E = 0
for s, e in time:
    if s >= E:
        ans += 1
        E = e
print(ans)