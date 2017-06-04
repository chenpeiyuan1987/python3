# 摄氏温度转华氏温度
# 用户输入摄氏温度

celsius = float(input("请输入摄氏温度："));

fahrenheit = (celsius * 1.8) + 32;
print("%0.1f 摄氏温度转为华氏温度为 %0.1f." % (celsius, fahrenheit));
