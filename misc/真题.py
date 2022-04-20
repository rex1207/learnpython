n=100000000000000000000000000000
while True:
    a = int(input())
    if a<60:
        print('不合格')
        n+=1
        continue
    elif a>=60 and a<85:
        print('良')
        n+=1
        continue
    elif a>=85 and a<101:
        print('优')
        n+=1
        continue

