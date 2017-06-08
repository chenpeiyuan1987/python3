# 最小公倍数

def calc(a,b):
    c = max(a,b);

    for n in range(c,a*b) :
        if(n % a == 0) and (n % b == 0):
            return n;

num1 = int(input("输入第一个数字："));            
num2 = int(input("输入第二个数字："));            

print(num1, "和", num2, "的最小公倍数是", calc(num1,num2));
