# 输入两个数，输出他们的公约数列表及公约数数量
# 输入
# 30
# 70
# 输出
# [1,2,5,10]
# 4
a=int(input())
b=int(input())
c=min(a,b)
d=[]
for i in range(1,c+1):
    if a%i==0 and b%i==0:
        d.append(i)
        continue
print(d)
print(len(d))
