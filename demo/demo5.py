# 求三角形的面积
# 用户输入三条边

a = float(input("请输入第一条边的长度："));
b = float(input("请输入第二条边的长度："));
c = float(input("请输入第三条边的长度："));

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5;

print("三角形面积为 %0.2f" % area);
