#  写一个函数，判断一个数是否为完全平方数
#  输入：4
#  输出：True
# 输入：10
#  输出：False

a=int(input(''))
flag = False
for i in range(0,a-1):
    if i*i==a:
        flag = True
        break
print(flag)
