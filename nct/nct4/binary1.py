a = int(input())
b = list(range(1, 100))
def ouch(a, item):
    first = 0
    last = len(item) - 1
    found = False
    while first <= last and not found:
        middle = (first+last)//2
        if item[middle]==a:
            found=True
        else:
            if a<item[middle]:
                last=middle-1
            else:
                first=middle+1
        print(first,last)
    return found
print(ouch(a,b))
