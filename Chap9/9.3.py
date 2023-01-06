def avoid(a,b):
    for x in a:
        if x in b:
            return False
    return True
print(avoid('hajsjakhsdbcuk','jsn'))