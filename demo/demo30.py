# 计算每个月天数

import calendar;
year = int(input("请输入年份："));
month = int(input("请输入月份："));
days = calendar.monthrange(year,month)[1];
print("%s年%s月有%s天" % (year,month,days));
