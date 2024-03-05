# 실수) return 대신 break로 벗어나게끔 했더니 2중 for문을 벗어나지 못한다는 점을 간과했다
# 풀이) 전치행렬 / check함수로 가능 유무 검사 / V배열을 통해 경사로 설치 가능 여부
# 리팩토링하자
def check(tlst):
    v = [0]*len(tlst) # 경사로 설치 여부
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
                    if v[i+1+k]==1: return 0
                    v[i + 1 + k] = 1
            else: break
        elif tlst[i] < tlst[i + 1]:  # 다음이 오르막
            if same >= L and v[i]==0:
                same = 1
                for k in range(L):
                    if v[i - k] == 1: return 0
                    v[i - k] = 1
            else: break
        elif tlst[i] == tlst[i + 1]:  # 다음이 평지
            same += 1
    else: return 1
    return 0

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_t = [list(lst) for lst in zip(*arr)]
ans = 0
for i in range(len(arr)):
    ans += check(arr[i])
    ans += check(arr_t[i])
print(ans)