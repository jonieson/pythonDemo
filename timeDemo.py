# -*- coding: UTF-8 -*-

import time
import calendar

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

# 将时间戳转换成时间格式
print time.strftime("%Y-%m-%d %H:%M:%s",time.localtime())



#----------------------日历------------------

cal = calendar.month(2017,7)
week = calendar.weekday(2017,7,11)
print "今天是第%d周",week
