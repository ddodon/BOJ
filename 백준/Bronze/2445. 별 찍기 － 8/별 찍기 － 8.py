N = int(input())
for i in range(1, (2 * N + 1)):
    if i <= N:
        print(("*" * i) + (" " * ((2 * N) - (2 * i))) + ("*" * i))
    else:
        print(("*" * (2 * N - i)) + (" " * ((2 * i) - (2 * N))) + ("*" * (2 * N - i)))