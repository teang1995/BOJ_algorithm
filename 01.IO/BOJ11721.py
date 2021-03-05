# 열 개씩 끊어 출력하기
word = input()
for i in range(len(word) // 10 + 1):
    print(word[10 * i: 10 * i + 10])
