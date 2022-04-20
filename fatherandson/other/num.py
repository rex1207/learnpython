#定义一个类，有两个属性start和end，int类型
#定义一个方法，计算start到end之间不包含数字1的一共有多少个
#输入start:1
#输入end:20
#输出：1到20之间不包含数字1的一共有9个
class A:
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def f(self):
        n=0
        for i in range(self.start,self.end+1):
            if '1' in str(i):
                n+=1
        print(str(self.start)+'到'+str(self.end)+'之间不包含数字一的一共有'+str(self.end-n)+'个。')
start=int(input())
end=int(input())
a=A(start,end)
a.f()