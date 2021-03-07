# 1로 만들기

N = int(input())
ans = [0 for _ in range(1000001)]
ans[1] = 0
ans[2] = 1
ans[3] = 1
for i in range(4, N + 1):
    if i % 6 == 0:
        ans[i] = min(ans[i // 2] + 1, ans[i//3] + 1, ans[i - 1] + 1)
    elif i % 2 == 0:
        ans[i] = min(ans[i // 2] + 1, ans[i - 1] + 1)
    elif i % 3 == 0:
        ans[i] = min(ans[i // 3] + 1, ans[i - 1] + 1)
    else:
        ans[i] = ans[i - 1] + 1
print(ans[N])