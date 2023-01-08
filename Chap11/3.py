def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))
#这个函数的增长非常块，（4，3）就已经无法确定位数了

known = {}#设定备忘录
def ack_memo(m,n):
    if (m,n)in known:
        return known[m,n]
    
    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return ack(m-1,1)
    
    elif  m>0 and n>0:
        known[m, n] = ack_memo(m-1, ack_memo(m, n-1))
        return known[m,n]

#ack_memo好像是要快一点，虽然是快一点进入到最大深度递归

print(ack_memo(4,3))

