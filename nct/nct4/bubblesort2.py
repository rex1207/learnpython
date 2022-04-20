a=input()
b=a.split(',')
c=[int(i) for i in b]
def bubblesort(c):
    for i in range(len(c)-1,0,-1):
        for j in range(i):
            if c[j]>c[j+1]:
                d=c[j]
                c[j]=c[j+1]
                c[j+1]=d
    return c
print(bubblesort(c))

