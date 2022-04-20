# 36.
# 实现统计字符串中的单词和单词出现的次数：
# 要求如下：
# （1）统计的语句为：to be or not to be that is a question
# （2）要求统计该句中出现的所有单词和其出现次数。
# （3）使用字典进行输出，格式如下（注意：排列顺序可以不一致，但是统计的次数要正确）：
# {'to': 2, 'be': 2, 'or': 1, 'not': 1, 'is': 1, 'a': 1, 'question': 1, 'that': 1}
a='to be or not to be that is a question'
b=a.split(' ')
c={}
for i in b:
    if i in c:
        c[i]=c[i]+1
    else:
        c[i]=1
print(c)



