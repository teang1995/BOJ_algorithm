# 별 찍기 - 9

N = int(input())
nums = [2 * i - 1 for i in range(N, 0, -1)] + [2 * i + 1 for i in range(1, N)]

for i, num in enumerate(nums):
    print(" " * ((2 * N - num) // 2) + "*" * num + " ")