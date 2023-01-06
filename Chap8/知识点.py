#字符串
fruit='banana'

fruit[0]#b
fruit[-1]#a
fruit[:5]#fruit--字符串切片
fruit[0:]#fruit

#while循环遍历字符串
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
    

#for循环遍历字符串
for letter in fruit:
    print(letter)
    
#字符串加法
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    print(letter + suffix)
    
    
#注：字符串内字符不可以修改，硬要改只能将其提取处理定义新的字符串

#搜索，也就是遍历过程中比对
def find(word, letter): #此函数意在发现word中letter的位置，若不存在则输出-1，存在则报点
    index = 0
    result_list=[]
    while index < len(word):
        if word[index] == letter:
            result_list.append(index) 
        index = index + 1
    return result_list

find('banana','a')#[1,3,5]


#循环计数
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
    print(count)#每个字母都过一遍，如果该字母==a，+1
    
    
#z字符串的一些方法

#1
#大写函数
word='banana'#BANANA
word.upper()#注意此函数不接受形参
#2
#查找函数
word.find('a')#1
word.fibd('na')#2,为字符串出现的第一个字母的字符位置
word.find('na',3)#4，指定了开始查找的位置
word.find('n',1,2)#-1,指定了开始和结束的位置


#in运算符
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)#找word1、word2的共同字母
