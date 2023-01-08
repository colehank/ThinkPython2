import os

def pipe(cmd):#用python写命令交给shell，并返回shell反馈
    fp = os.popen(cmd)#shell打开cmd
    res = fp.read()#读取shell反馈
    stat = fp.close()#程序是否关闭
    #print (res, stat)#返回反馈以及程序已关闭
    assert stat is None
    return res,stat
      



def walk(dirname):
#"把目录下所有文件名和文件内的目录的文件名打印出来"
    names = []
    
    for name in os.listdir(dirname):#返回指定文件夹里的文件或文件夹的名字列表
        path = os.path.join(dirname, name)#将目录和文件名拼接为一个完整的路径
        if os.path.isfile(path):#判断绝对路径下是否是一个文件///文件名可以是相对路径
            names.append(path)
        else:
            names.extend(walk(path))
    return names  
  
 
#walk('/Users/harrischeung/Documents/GitHub/think_python/Chap14')

#注意，要安装MD5，unix：brew install md5sha1sum

def checksum1(filename):
    cmd = 'md5sum %s' %filename
    #%d用于int，%g用于float，%s用于字符串
    return pipe(cmd)

#checksum('words.txt')

def diff(name1, name2):
    #计算两个文件的差异
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)

#diff('sed.py','words.txt')

'##########################以下不懂，暂时抄的答案######################################################'
def checksums_all(dirname, suffix):
    #检查目录下所有相同后缀文件的校验值，返回校验值以及有这个校验值的文件列表的映射
    names = walk(dirname)
    d = {}
    for name in names:
        if name.endswith(suffix):#endswith检查字符串是否以指定后缀结（suffix）尾
            res, stat = checksum1(name)
            checksum, _ = res.split()#split（）按括号内分割
            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]
    return d

#checksums_all('/Users/harrischeung/Documents/GitHub/think_python/Chap14','.py')


def check_pairs(names):#names：字符串文件的列表
    """Checks whether any in a list of files differs from the others.
    names: list of string filenames
    """#检查文件中列表里的内容是否和其他的不一样
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = diff(name1, name2)
                if res:
                    return False
    return True


def print_duplicates(d):
    """Checks for duplicate files.
    Reports any files with the same checksum and checks whether they
    are, in fact, identical.
    d: map from checksum to list of files with that checksum
    """#检查是否有文件的校验值一样，检查他们是否真正的相同
    for key, names in d.items():
        if len(names) > 1:
            print('The following files have the same checksum:')
            for name in names:
                print(name)

            if check_pairs(names):
                print('And they are identical.')
                
                
d = checksums_all('/Users/harrischeung/Documents/GitHub/think_python/Chap14','.txt')
print_duplicates(d)

#unix的diff功能：diff a b，若无返回值，则说明一样

