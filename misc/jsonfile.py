import json
with open('test.json', 'w') as file:
    for i in range(10000000):
        json.dump('hello'+str(i)+'*'*20, file)