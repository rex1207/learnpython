print('my'.title() +' name is '+'wang si yue'.title())
print('i'.title()+' was born on December 7,2009.')
print('my'.title()+' favourite color is Sky Blue.')


import random
number=random.randint(0,500)
guess_number=0
tries=0
print('hello'.title()+'!i'.title()+' am Wang.'+'i'.title()+' will ask you a question.'+'\ni'.title()+' will give you a number from 0 to 500, and you should guess!'+'i'.title()+' will give you ten times.')
while guess_number!=number and tries<10:
    guess_number=int(input('What number do you guess?'))
    if guess_number<number:
        print('oh'.title()+' your number is too small,try another one please！')
    elif guess_number>number:
        print('oh'.title()+' your number is too big,try another one please!')
    tries=tries+1
if guess_number==number:
    print('OhOhOh'*2+'!　you'.title()+' are right!'+'congratulations!'.title())
else:
    print('do'.title()+' not give up！'+'perhaps'.title()+' you will be lucky the next time!')
print('the'.title()+' ture answer is　number', number)








