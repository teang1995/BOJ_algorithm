# 2 x n 타일링2

N = int(input())
ans = [0 for i in range(1001)]
ans[1] = 1
ans[2] = 3
for i in range(3, N + 1):
    ans[i] = ans[i - 2] * 2 + ans[i - 1]
print(ans[N] % 10007)
