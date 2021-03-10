# 쉬운 계단 수

N = int(input())
ans = [0 for _ in range(101)]
ans[1] = 9
ans[2] = 17
for i in range(2, N + 1):
    ans[i] = 2 * ans[i - 1] - i
print(ans[N])
# wrong, tomorrow