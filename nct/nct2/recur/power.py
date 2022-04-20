#递归求幂
#x的n次幂=x*x*...*x 一共n个x相乘
# 输入x和n
# 3
# 4
# 输出81
def f(x,n):
    if n==1:
        return x
    else:
        return f(x,n-1)*x
x=int(input())
n=int(input())
print(f(x,n))