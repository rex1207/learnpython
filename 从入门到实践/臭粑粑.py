"""
this is comment
"""
# this is also comment
a=input('choubaba')
num_list =a.split(' ')
total =0
for i in num_list:
    try:
        total += int(i)
    except:
        print('error', i)
print(total)



