# 二次方程 ax**2 + bx + c = 0
# 用户输入 a,b,c

import cmath;

a = float(input("输入 a："));
b = float(input("输入 b："));
c = float(input("输入 c："));

d = (b ** 2) - (4 * a * c);

r1 = (-b - cmath.sqrt(d)) / (a * 2);
r2 = (-b + cmath.sqrt(d)) / (a * 2);

print("结果为 {0} 和 {1}".format(r1,r2));
