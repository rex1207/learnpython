import turtle as t
def f(n):
    if n > 0:
        t.forward(n)
        t.right(20)
        f(n-20)
        t.left(40)
        f(n-20)
        t.right(20)
        t.backward(n)


t.left(90)
t.up()
t.backward(200)
t.down()
t.color('green')
f(100)
t.hideturtle()
t.done()