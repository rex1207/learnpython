# 使用for循环，求从1到300的自然数，不包含数字1的一共有多少个
# a=1
# b=[]
# for i in range(1,301,1):
#
#     if '1' not in str(i):
#         b.append(i)
# print(b)
# print(len(b))


class Num:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_number(self):
        b = []
        for i in range(self.start, self.end+1, 1):
            if '1' not in str(i):
                b.append(i)
        print(b)
        print(len(b))
        return len(b)


num = Num(100,300)
num.get_number()