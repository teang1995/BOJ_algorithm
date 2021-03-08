# 1, 2, 3 더하기

N = int(input())
ans = [0 for _ in range(11)]
ans[1] = 1
ans[2] = 2
ans[3] = 4
for _ in range(N):
    n = int(input())
    if ans[n] != 0:
        print(ans[n])
    else:
        i = 1
        while ans[i] != 0:
            i += 1
# 응 내일 할 거야~
