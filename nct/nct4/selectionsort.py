ouch=input()
ooooo=ouch.split(',')
oucher=[int(i) for i in ooooo]
def selection(oucher):
    for i in range(len(oucher)-1,0,-1):
        index=0
        for j in range(1,i+1):
            if oucher[j]>oucher[index]:
                index=j
        ouchest=oucher[i]
        oucher[i]=oucher[index]
        oucher[index]=ouchest
    return oucher
print(selection(oucher))