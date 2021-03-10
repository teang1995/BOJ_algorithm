# 1, 2, 3 더하기

N = int(input())
ans = [0 for _ in range(11)]
ans[1] = 1
ans[2] = 2
ans[3] = 4
for i in range(4, 11):
    ans[i] = ans[i - 1] + ans[i - 2] + ans[i - 3]
for _ in range(N):
    num = int(input())
    print(ans[num])

# 응 내일 할 거야~
