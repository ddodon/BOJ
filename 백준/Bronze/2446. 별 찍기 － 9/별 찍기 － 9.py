N = int(input())
for i in range(2 * N-1):
    if i < N:
        print((" " * i) + ("*" * ((2 * N - 1) - 2 * i)))
    else:
        print(" "*((2 * N - 1)-(i+1))+"*"*((2*i)-(2*N-3)))