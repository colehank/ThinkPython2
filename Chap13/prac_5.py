def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0)+1#键值等于项目返回的值+1，若不存在，默认值为0+1就新建，若存在，键值+1便计数
    return d


#%%

import random

"不理解，既然字母在单词的数量和单词总字母量确定，为什么不直接随机选取，那就是它被选的概率啊"
"因为要用hist做，就再把它逆转回去"
def choose_from_hist(hist):
    p = list()
    for key, value in hist.items():
        for i in range(value):
            p.append(key)
    return random.choice(p)



print(choose_from_hist(histogram("didjfhjsknc")))



