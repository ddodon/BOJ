'''
Memo BOJ 16987 계란으로 계란치기
손에 든 계란이 깨진다 / 친 계란이 깨진다 / 둘 다 깨진다 / 둘 다 안 깨진다
* 2번 테스트 케이스의 경우: 세번째 계란을 집으면 나머지는 다 깨져 있다 -> dfs(n+1) 해줘야 함
최대값을 구할 때의 가지치기가 가능한가?
'''


# 순서 / 현재 계란 내구도 / 현재 계란 무게 / 현재 계란 번호
def dfs(n):
    global ans
    if n == N:
        cnt = 0
        for i in range(N):
            if arr[i][0] <= 0:
                cnt += 1
        ans = max(ans, cnt)
        return

    # 현재 손에 든 계란이 깨진 경우
    if arr[n][0] <= 0:
        dfs(n + 1)
        return

    # 현재 손에 든 계란 제외 다 깨진 경우
    if arr[n][0] > 0:
        tmp = 0
        for t in range(N):
            if arr[t][0] <= 0:
                tmp += 1
        if tmp == N - 1:
            dfs(n + 1)

    # 계란 깨기
    for j in range(N):
        # 자기 자신이 아니고 + 칠 계란이 깨진 경우가 아님
        if n != j and arr[j][0] > 0:
            arr[n][0] -= arr[j][1]
            arr[j][0] -= arr[n][1]
            dfs(n + 1)
            arr[n][0] += arr[j][1]
            arr[j][0] += arr[n][1]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0)
print(ans)