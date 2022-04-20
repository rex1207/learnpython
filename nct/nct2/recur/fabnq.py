def f(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return f(n-2)+f(n-1)

n=int(input())
print(f(n))
