# 递归实现斐波那契数列

def fibo(n):
    if n <= 1:
        return n;
    else:
        return fibo(n-1) + fibo(n-2);

nterms = int(input("您要输出几项："));

if nterms <= 0:
    print("请输入正数");
else:
    print("斐波那契数列：");
    for i in range(nterms):
        print(fibo(i));
