a=['啊！','干!','啥！']
print(a)
a[0]='aaa'
print(a)
a.insert(0,'干啥啊！')
print(a)
a.insert(2,'啊呀！')
print(a)
a.append('55555555......')
print(a)
jj=a.pop(0)
print(jj)
print(a)
jj=a.pop()
print(jj)
print(a)
del a[0]
print(a)
a.remove('啊呀！')
print(a)
if 'aaaaa'  in a:
    a.remove('aaaaa')
print(a)
a.pop(10)