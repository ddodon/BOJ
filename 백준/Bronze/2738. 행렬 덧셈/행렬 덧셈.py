n,m = map(int,input().split())
matrix_a = []
matrix_b = []
for i in range(n):
    a = list(map(int,input().split()))
    matrix_a.append(a)
for i in range(n):
    b = list(map(int,input().split()))
    matrix_b.append(b)
for i in range(n):
    for j in range(m):
        matrix_a[i][j] = matrix_a[i][j]+matrix_b[i][j]

for i in range(n):
    print(*matrix_a[i])