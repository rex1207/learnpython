r = range(1,10)
print(type(r))
l = list(r)
print(type(l))
print(l)
for s in l:
    if s==1:
        print('1st')
    elif s==2:
        print('2nd')
    elif s==3:
        print('3rd')
    else:
        print(str(s) + 'th')
