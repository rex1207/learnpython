a = 'how old are you?'
b = True
while b:
    age = int(input(a))
    if age < 3:
        print('you do not need to pay for the ticked')
    elif age > 3 and age < 12:
        print('you need to pay 10 yuan for the ticked')
    else :
        print('you need to pay 15 yuan for the ticked')
        break
