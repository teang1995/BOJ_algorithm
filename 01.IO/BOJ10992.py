# 별 찍기 - 17

N = int(input())
for i in range(1, N):
    print(" " * (N - i), end="")
    for j in range(1, 2 * i):
        if j in [1, 2 * i - 1]:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
print("*" * (2 * N - 1))