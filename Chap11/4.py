from 知识点 import histogram_better

def hd(t):
    fin = histogram_better(t)#搬用计数器函数，只要计数有>=2的值便是重复
    val = fin.values()
    for i in range(len(t)):#只用确定i大于等于二就行，这里用单词长度作为循环范围
        if i+2 in val:#循环从0开始，i+2>=2,若i+2存在val，足以说明重复
            return True
    else:
        return False
    

t=['a',1,'d',3,4]
histogram_better(t)

print(hd(t))
