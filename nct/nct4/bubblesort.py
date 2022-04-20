ouch=input()
a=ouch.split(',')
c= [int(i) for i in a]
def bubble(c):
    for i in range(len(c)-1,0,-1):
        for j in range(i):
            if c[j]>c[j+1]:
                # b=c[j]
                # c[j]=c[j+1]
                # c[j+1]=b
                c[j], c[j + 1] = c[j + 1], c[j]
    return c
print(bubble(c))
