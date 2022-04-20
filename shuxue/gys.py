# 求两个数的所有公因数列表
# 输入：
# 100
# 120
# 输出：[1,2,5,10,20]
a=int(input(''))
b=int(input(''))
c=[]
d=min(a,b)
for i in range(1,d):
    if a%i==0 and b%i==0:
        c.append(i)
print(c)

