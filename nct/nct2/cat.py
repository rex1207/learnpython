# 请按照下列要求编写程序。
#
# 1.创建一个猫类，属性:姓名；
#
# 2.创建老鼠类，属性：姓名；
#
# 3.输出一只名叫xxx的猫抓到了一只名叫xxx的老鼠；
#
# 4.输入猫的名字和老鼠的名字。
#
# 输入：
#
# Tom
#
# Jerry
#
# 输出：
#
# 一只名叫Tom的猫抓到了一只名叫Jerry的老鼠
a=input()
b=input()
class Cat():
    def __init__(self,name):
        self.name=name


class Mouse():
    def __init__(self,name):
        self.name=name


cat=Cat(a)
mouse=Mouse(b)
print('一只叫'+cat.name+'的猫抓住了一只叫'+mouse.name+'的老鼠。')
