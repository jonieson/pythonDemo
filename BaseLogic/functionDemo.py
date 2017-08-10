# -*- coding: UTF-8 -*-

#定义函数
def printParama(str):
    print str
    return ;
#调用函数
printParama('i love code')

#类型属于对象，变量是没有类型的

a = [1,2,3,4]   #[1,2,3,4]是list类型
a = 'hello jonieson'    #hello jonieson'是string类型
#a是变量不属于类型
print a

#不可变参数传递
def changeInt(num):
     num = 10

numTwo = 2
changeInt(numTwo)
print numTwo

#可变参数传递
def changeArr(arr):
    arr.append(5)
    print '函数内打印：%s' %arr
    return
list = [1,2,3,4]
changeArr(list)
print '函数外打印:%s'% list