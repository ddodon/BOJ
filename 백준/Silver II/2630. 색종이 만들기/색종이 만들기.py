'''
Memo BOJ 2630 색종이 만들기
분할정복 문제
* 다른 풀이: any() 함수 사용법 익혀두기
'''

# 시작좌표 / 한 변의 길이
def dnc(si,sj,n):
    global w_lst
    global b_lst

    # 종료조건: 모두 같은 색
    cnt = 0
    for i in range(si,si+n):
        for j in range(sj,sj+n):
           cnt += arr[i][j]
     # 모두 파란색
    if cnt == n**2:
        b_lst +=1
        return
    elif cnt == 0:
        w_lst += 1
        return

    # 분할
    m = n//2
    dnc(si, sj, m)
    dnc(si+m, sj, m)
    dnc(si, sj+m, m)
    dnc(si+m, sj+m, m)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

b_lst = 0
w_lst = 0
dnc(0, 0, N)
print(w_lst)
print(b_lst)