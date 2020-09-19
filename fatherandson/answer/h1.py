# 从1到300的自然数，不包含数字1的一共有多少个
count = 0
for i in range(1, 301):
    s = str(i)
    # print(s)
    if "1" not in s:
        print(s)
        count += 1
print(count) 