def check(tlst):
    v = [0]*len(tlst) # 경사로 설치 여부
    flag = False #경사로 필요 여부
    same = 1
    for i in range(len(tlst) - 1):
        if tlst[i] > tlst[i + 1] + 1: break
        if tlst[i] + 1 < tlst[i + 1]: break

        if tlst[i] > tlst[i + 1]:  # 다음이 내리막
            same = 1
            for j in range(i+1,len(tlst)-1):
                if tlst[j] == tlst[j+1]:
                    same += 1
                else: break
            if same >= L:
                same = 1
                for k in range(L):
                    if v[i+1+k]==1:
                        return 0
                    v[i + 1 + k] = 1
            else: break
        elif tlst[i] < tlst[i + 1]:  # 다음이 오르막
            if same >= L and v[i]==0:
                same = 1
                for k in range(L):
                    if v[i - k] == 1:
                        return 0
                    v[i - k] = 1
            else: break

        elif tlst[i] == tlst[i + 1]:  # 다음이 평지
            same += 1
    else:
        return 1
    return 0


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_t = [list(lst) for lst in zip(*arr)]
ans = 0

# for lst in arr:
#     print(lst)

for i in range(len(arr)):
    ans += check(arr[i])
    # print(f'{i+1} 회차  정방향 {ans} -- {arr[i]}')
    ans += check(arr_t[i])
    # print(f'{i+1} 회차  전치방향 {ans} -- {arr_t[i]}')
print(ans)