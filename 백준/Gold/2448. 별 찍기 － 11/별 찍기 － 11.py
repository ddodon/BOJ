'''
Memo 2448 별 찍기 11
또 공백으로 장난질
*  뒤에 공백밖에 남은 것이 없더라도 다 출력해줘야 합니다. 그러지 않으면 "출력 형식이 잘못되었습니다"를 받습니다.
분할정복
전 코드와 다른 점 파악하기
'''

def dnc(n):
    # 종료조건
    if n == 3:
        return ["  *  ", " * * ", "*****"]

    m = n // 2
    lst = dnc(m)
    res = []
    for l in lst:
        res.append(' ' * m + l + ' ' * m)
    for l in lst:
        res.append(l + ' ' + l)
    return res

N = int(input())
arr = dnc(N)
for a in arr:
    print(''.join(a))