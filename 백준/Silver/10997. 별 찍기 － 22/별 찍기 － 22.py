'''
Memo 10997 별 찍기 22
또 공백으로 장난질
방향 순서대로
* 실수) 코드대로라면 N==1 일때, 별이 3개 나온다. 아마 재귀로 푸는 방식인데 단순 구현해서 그런듯
'''

# 이동방향
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

# 입력 / 별 찍기 배열 / 두 줄 두르기
N = int(input())
r = 3 + (4 * (N - 1))
c = 1 + (4 * (N - 1))
arr = [['*' for _ in range(c + 4)]] + [[' ' for _ in range(c + 4)]] + \
      [['*'] + [' '] + [' ' for _ in range(c)] + [' '] + ['*'] for _ in range(r)] + \
      [[' ' for _ in range(c + 4)]] + [['*' for _ in range(c + 4)]]
if N == 1:
    print('*')
else:
    # 우측 끝부터
    k = 0
    i = 2
    j = c + 2
    cnt = 0
    while 1:
        ni = i + di[k]
        nj = j + dj[k]
        nni = ni + di[k]
        nnj = nj + dj[k]
        if arr[nni][nnj] == '*':
            k = (k + 1) % 4
            cnt += 1
            if cnt >= 4:
                break
        else:
            arr[ni][nj] = '*'
            i, j = ni, nj
            cnt = 0
    for lst in arr[2:-2]:
        print("".join(lst[2:-2]).rstrip())