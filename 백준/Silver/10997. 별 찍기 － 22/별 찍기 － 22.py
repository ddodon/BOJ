di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

N = int(input())
r = 3 + 4 * (N - 1) if N > 1 else 1
c = 1 + 4 * (N - 1)
arr = [[' '] * c for _ in range(r)]

ci = 0
cj = c - 1
k = 0
ei = r - 1 - (N - 1) * 2
ej = c // 2
arr[ci][cj] = '*'

while 1:
    ni = ci + di[k]
    nj = cj + dj[k]

    if (ci, cj) == (ei, ej):
        break

    if not (0 <= ni < r and 0 <= nj < c):
        k = (k + 1) % 4
        continue
    if arr[ni][nj] == '*':
        arr[ci][cj] = ' '
        ci = ci - di[k]
        cj = cj - dj[k]
        k = (k + 1) % 4
        continue
    arr[ni][nj] = '*'
    ci = ni
    cj = nj

for a in arr:
    print(''.join(a).rstrip())