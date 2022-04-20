# 3、求两个整数的最小公倍数
# 输入
# 16
# 12
# 输出
# 48
a=int(input(''))
b=int(input(''))
for i in range(1,a*b+1):
    if i%a==0 and i%b==0:
        print(i)
        break

