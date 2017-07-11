# -*- coding: UTF-8 -*-
for letter in 'python' :
    print '当前字母:'+letter

array = ['hello','world','you','are','best']
for name in array:
    print '元素:'+name

#根据索引获取数组元素
fruitArr = ['banana','apple','orange','welenter']
for index in range(len(fruitArr)):
    print '当前水果：'+fruitArr[index]

#for循环嵌套for...else:else代表当for执行完后正常跳出再执行
for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j = num/i
            print '%d 等于 %d *%d'%(num,i,j)
            break
    else:
        print num,'这是一个质数'
#打印数组索引以及对应的值（函数）
testArr = ['value1','value2','value3','value4','value5','value6','value7']
for index,value in enumerate(testArr):
    print '索引:',index,'值:',value
else:
    print '索引值对打印完毕'