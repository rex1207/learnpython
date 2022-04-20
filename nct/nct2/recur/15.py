a=input()
b=a.split(',')
c=[]
def f():
    for i in b:
        c.append(int(i))
f()
print(c)