##setdefault和get的区别：前者就在原字典存入键值对，后者只返回默认值，其他一样
'字典.get（key，默认值）：获得字典键的键值，若不存在键，返回默认值'
'字典.setdefault（key，默认值）：获得字典键的键值，若不存在键，写入此输入的键值对,并返回默认值'

from 知识点 import histogram_better

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse.setdefault(val, key)
        else:
            inverse[val].append(key)#行不通
    return inverse


#%%
def invert_shorter(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)# setdefault返回的是一个空列表，在此基础上可以直接append
    return inverse

hist = histogram_better('brontosaurus')
inverse = invert_shorter(hist)

print(inverse)
