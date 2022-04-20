def f(n):
    if n < 2:
        return 1
    else:
        return n*f(n-1)
a=int(input())
x=0
for i in range(a+1):
    x+=f(i)
print(x)