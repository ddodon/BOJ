from collections import deque
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    lst = input()
    number_list = set()

    for i in range(0,N,N//4):
        number_list.add(int(lst[i:i+(N//4)],16))

    for _ in range(N//4):
        dq = deque(lst)
        dq.rotate(1)
        lst = list(dq)
        for i in range(0, N, N // 4):
            s = ''
            for j in lst[i:i + (N // 4)]:
                s += j
            number_list.add(int(s, 16))

    print(f'#{test_case} {sorted(list(number_list),reverse=True)[K-1]}')