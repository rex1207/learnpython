import json
filename = 'number.json'
with open(filename, 'w') as f:
    number = int(input())
    a={
        'name':'ba',
        'age':number
    }
    json.dump(a,f)
print(type(f))
with open(filename) as f:
    a = json.load(f)
    print("I know your favorite number! It's "+str(a)+'!'+str(type(a)))




