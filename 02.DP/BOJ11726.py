# 2 x n 타일링

N = int(input())
ans = [0 for _ in range(1001)]
ans[1] = 1
ans[2] = 2
for i in range(3, N + 1):
    ans[i] = ans[i - 1] + ans[i - 2]
print(ans[N] % 10007)
