# 1.定义一个手机类，手机类的属性有型号，内存大小，售价；
# 2.定义一个苹果类：继承手机类，并增加属性“屏幕大小”，增加打印方法，打印手机售价；
# 3.运行程序，分别输入手机的型号，内存大小，售价，屏幕大小，输出该手机的售价
# 输入格式：请输入型号：xxx 请输入内存大小：xxx 请输入售价：xxx  请输入屏幕大小：xxx
# 输出格式： 型号：xxx，内存大小：xxx，屏幕大小：xxx
# 该型号手机售价是： xxx
class Phone:
    def __init__(self,x,n,s):
        self.x=x
        self.n=n
        self.s=s

class Apple(Phone):
    def __init__(self,x,n,s,big):
        super().__init__(x,n,s)
        self.big = big

    def f(self):
        print('型号：'+self.x+'，内存大小：'+self.n+'，屏幕大小：'+self.big)
        print('该型号手机售价为：'+self.s+'。')

x=input('请输入型号：')
n=input('请输入内存大小：')
s=input('请输入售价：')
big=input('请输入内存大小：')
apple=Apple(x,n,s,big)
apple.f()

