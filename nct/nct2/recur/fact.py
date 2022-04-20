# 定义个函数递归求n的阶乘
# n!=n*(n-1)*...*1
# 输入5
# 输出120
def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
print(f(int(input())))
