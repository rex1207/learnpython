import matplotlib.pyplot as plt
import random
import math
radius = 1
d = 2 * radius
rect = 0
circle=0
ratio = 0


def create_circle():
    return plt.Circle((0,0), radius=radius, fill=False)


def distance(p1, p2):
    global rect
    global circle
    if ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(1/2)>radius:
        rect += 1
    elif ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(1/2)<radius:
        circle += 1
    # print(str(circle)+":"+str(rect))
    print('落在圆内部的小圆点数量:{} vs 落在外部的小圆点数量:{}'.format(circle, rect))


def create_inner_circle(n):
    patches = []
    for i in range(n):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        p1=(x,y)
        p2=(0,0)
        distance(p1,p2)
        patches.append(plt.Circle((x,y), radius=0.01 * radius))
    return patches


def create_rect():
    return plt.Rectangle((-radius, -radius), 2 * radius, 2 * radius, fill=False)


def show_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')


def show_shapes(patches):
    ax = plt.gca()
    for patch in patches:
        ax.add_patch(patch)
    plt.axis('scaled')


if __name__ == '__main__':
    plt.rcParams["font.sans-serif"] = "KaiTi"
    plt.rcParams["axes.unicode_minus"] = False
    number = int(input('请输入小圆点的数量：'))
    print('系统启动中，请稍等。。。。。。')
    show_shapes(create_inner_circle(number))
    show_shape(create_rect())
    show_shape(create_circle())
    ratio = circle/number
    square_area = math.pi*(radius ** 2)
    rect_area = d ** 2
    estimate_area = rect_area*ratio
    print('程序运行完毕，估算出来的单位圆面积（PI值）是：'+str(estimate_area))
    plt.title('圆实际面积:{} 蒙特卡洛估算圆面积或PI值(正方形面积*落在圆内部随机点的比例)：{}*{}={}'.format(round(square_area,2), rect_area, ratio, estimate_area))
    plt.show()