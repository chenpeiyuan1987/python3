# 最大公约数

def calc(a,b):
    c = min(a,b);

    for n in range(c,0,-1):
        if((a % n == 0) and (b % n == 0)):
            return n;

num1 = int(input("输入第一个数字："));            
num2 = int(input("输入第二个数字："));            
print(num1, "和", num2, "最大公约数", calc(num1,num2));
