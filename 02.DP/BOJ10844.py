# 쉬운 계단 수

N = int(input())
ones = [0 for _ in range(101)]
twos = [0 for _ in range(101)]
ones[1] = 7
twos[1] = 2
for i in range(2, N + 1):
    ones[i] = 2 * ones[i - 1] - 1
    twos[i] = i
    print(i)
ans = ones[N] + twos[N]
print(ans % 1000000000)
