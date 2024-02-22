'''
Memo 12904 A와 B
연산을 반대로 적용 (그냥 A떼기, B떼고 뒤집기)
항상 최적이 되는 연산
'''
def cal_A(s):
    return s[:-1]
def cal_B(s):
    return s[:-1][::-1]

s = input()
t = input()
while 1:
    if len(s) == len(t):
        break
    if t[-1] == 'A':
        t = cal_A(t)
    elif t[-1] == 'B':
        t = cal_B(t)
# print(s, t)
if s == t:
    print(1)
else:
    print(0)