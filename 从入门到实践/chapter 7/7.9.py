sandwich_orders = ['meat','fish','tomato']
finished_sandwiches = []
print("There are not any pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    finished_sandwiches.append(sandwich)

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
