import math
print('hello qua')
def quadratic(a, b, c):
    key = b**2-4*a*c
    if key > 0:
        x1 = round((-b+math.sqrt(key))/2*a, 1)
        x2 = (-b-math.sqrt(key))/2*a
    if key == 0:
        x1 = round(-b/2*a, 2)
        x2 = x1
    if key < 0:
        print('方程无解')
        return(None)
    return (round(x1, 1), round(x2, 1))


