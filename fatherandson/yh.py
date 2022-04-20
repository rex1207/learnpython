import turtle as T
import random
import time
# 画樱花的躯干(60,t)
def Tree(branch, t):
    time.sleep(0.0005)
    if branch > 7:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('white')  # 白
            else:
                t.color('pink')  # 淡珊瑚色
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('deep pink')  # 淡珊瑚色
            t.pensize(branch / 2)
        else:
            t.color('sienna')  # 赭(zhě)色
            t.pensize(branch / 10)  # 6
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()

# 掉落的花瓣
def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')  # 淡珊瑚色
        t.circle(2.5)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)

# 绘图区域
t = T.Turtle()
# 画布大小
w = T.Screen()
t.hideturtle()  # 隐藏画笔
t.getscreen().tracer(5, 0)
# t.speed(0)
w.screensize(bg='wheat')  # wheat小麦
# w.bgpic("1.png")
t.left(90)
t.up()
t.backward(200)
t.down()
# 画樱花的躯干
Tree(70, t)
# 掉落的花瓣
Petal(300, t)
T.color('red')
T.up()
T.right(180)
T.fd(150)
T.right(180)
T.fd(-100)
T.left(90)
T.fd(-180)
T.down()
T.write('妈妈，教师节快乐！', font=("KaiTi", 30, ""))
T.hideturtle()
w.exitonclick()