# 判断闰年

year = int(input("请输入年份："));

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("{0}是闰年".format(year));
        else:
            print("{0}不是闰年".format(year));
    else:  
        print("{0}是闰年".format(year));
else:
    print("{0}不是闰年".format(year));
