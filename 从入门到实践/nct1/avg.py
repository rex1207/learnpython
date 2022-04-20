# 2、一次性输入若干个整数（空格隔开），输出所有数字之和
# 输入
# 2 3 4 5 6 7 8 9
# 输出
# 44

a=input()
b=a.split(' ')
d=0
for i in b:
    d+=int(i)
print(d)
c=round(d/len(b))
print(c)