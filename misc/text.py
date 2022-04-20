with open('test.txt', 'w') as file:
    for i in range(1, 10000001):
        file.write('hello'+str(i)+'*'*20)
        file.write('\n')