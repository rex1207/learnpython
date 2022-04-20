# 请按照下列要求将代码补充完整：
#
# 1.定义一个“人”类（People），该类包含两个属性及三个方法，如下所示：
#
# （1）属性
#
# 姓名（name）
#
# 年龄（age）
#
# （2）方法
#
# work()，打印“working”
#
# get_name()，打印姓名
#
# get_age()，打印年龄
#
# 2.定义一个“学生”类（Student）
#
# （1）继承People类的属性和方法
#
# （2）重写work()方法,修改为打印“studying”

class People():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def work(self):
        print('working')

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

a=People('为何王如此帅',13)
a.work()
a.get_age()
a.get_name()


class Student(People):
    def work(self):
        print('studying')
b=Student('为何王如此帅',13)
b.work()
