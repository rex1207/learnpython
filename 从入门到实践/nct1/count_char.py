# 输入一个字符串，统计a字母出现的次数
# 输入
# abcdeAabb
# 输出
# 2

a=input('输入一个字符串')
b=0
for i in a:
    if i=='a':
        b+=1
print(b)