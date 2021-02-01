a=['shuai','wang','zai','zou','sao']
print(a[:3])
print(a[-3:])
b=a[:]
print(b)
a.append('zhang')
print(a)
print(b)
b.append('zhang')
print(b)
if 'wang' in a:
    print('yes')
else:
    print('no')


