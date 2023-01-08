#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:42:48 2023

@author: harrischeung
"""


def sed (Str_O,Str_N,file_1,file_2):
    #Str_1是旧字符串，Str_2是新字符串，file_1是被读取文件，file_2是写入被文件
    f_2 = open(file_2,'w+')
    f_1 = open(file_1,'r+')#'r'只读、'w'新建只写，'r+'读写，若不存在file报错，'a'附加写，'a+'附加读写，'w+'读写，若不存在file创建
    for i in f_1:
        i = i.replace(Str_O, Str_N)#字符串方法：replace(旧值，新值)
        f_2.write(i)
    f_2.close()
    f_1.close()


abc = open('abc.txt','w')
line = "dfihagkfilahfildhalahflialhla发嗲说u恶化我复合肥fhueihuf"
abc.write(line)
abc.close()

sed('a', '😊', 'abc.txt','colehank.txt')
            


            
            
