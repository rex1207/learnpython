if __name__ == '__main__':
    n = int(input())
    list=[]
    for i in range(n):
        a,*b=input().split()
        if a=='print':
            print(list)
        elif a=='insert':
            list.insert(int(b[0]),int(b[1]))
        elif a=='remove':
            list.remove(int(b[0]))
        elif a=='append':
            list.append(b[0])
        elif a=='sort':
            list.sort()
        elif a=='pop':
            list.pop()
        elif a=='reverse':
            list.reverse()
        print(list)