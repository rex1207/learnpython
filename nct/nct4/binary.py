a = int(input())
b = list(range(1, 100))
def laiba(a, items):
    first = 0
    last = len(items) - 1
    found = False
    while first <= last and not found:
        middle = (first + last) // 2
        if items[middle] == a:
            found = True
        else:
            if a < items[middle]:
                last = middle - 1
            else:
                first = middle + 1
        print(first, last)
    return found
print(laiba(a,b))







