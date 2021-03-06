sandwiches=['meat','fish','tomato']
ok_sandwiches=[]
while sandwiches:
    sandwich=sandwiches.pop()
    print('your '+sandwich+' sandwich is ok.')
    ok_sandwiches.append(sandwich)

for ok_sandwich in ok_sandwiches:
    print(ok_sandwich.title())