from chap11_知识点 import histogram_better


def list_frequent(s):
    t = []
    h = histogram_better(s)#返回的是{字母：数字}这样的字典
    for let, num in h.items():
        t.append((num, let))#注意括号，拓展的是元组,num放前面因为要按照num排序
    return t#如果直接倒序，不给结果，列表需要新建一个传入倒序t
#返回的是以元组为元素的列表

#print(list_frequent('banana'))



def sort_frequent(s):
    t = list_frequent(s)#以元组为元素的列表
    t1 = []
    t.sort(reverse=True)#reverse=True:倒序，sort函数的可选参数
    for i in t:#备忘：这里i只有1就指代元组，若2个就指代元组内的元素
        t1.append(i)#将倒序后的t传入新字典
    return t1


fout = open('words.txt').read#不read后面函数就就以每个词为单位遍历了，这样计数的是每个词出现的次数
def count_letter():
    for i in sort_frequent(fout):
        print(i)
        
count_letter()#输出中，\n为换行符 