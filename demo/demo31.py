# 获取昨日日期

import datetime;

def getYesterday():
    today = datetime.date.today();
    oneday = datetime.timedelta(days=1);
    yesterday = today - oneday;
    return yesterday;

print(getYesterday());    

