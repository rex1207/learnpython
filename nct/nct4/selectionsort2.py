ouch=input()
oucher=ouch.split(',')
ouchest=[int(i) for i in oucher]
def selection(ouchest):
    for i in range(len(ouchest)-1,0,-1):
        ouching=0
        for j in range(1,i+1):
            if ouchest[j]>ouchest[ouching]:
                ouching=j
        chest=ouchest[i]
        ouchest[i]=ouchest[ouching]
        ouchest[ouching]=chest
    return ouchest
print(selection(ouchest))

