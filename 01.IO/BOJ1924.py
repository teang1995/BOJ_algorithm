# 2007 년

x, y = map(int, input().split())

day = 0
day_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

for i in range(1, x):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        day += 31
    elif i in [4, 6, 9, 11]:
        day += 30
    else:
        day += 28
day += y - 1
print(day_list[day % 7])