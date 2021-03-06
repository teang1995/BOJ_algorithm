# 별 찍기 - 12

N = int(input())
nums = [i for i in range(1, N)] + [N] + [i for i in range(N -1, 0, -1)]
for i in nums:
    print(" " * (N - i) + "*" * i)