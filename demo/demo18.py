# 斐波那契数列

nterms = int(input("你需要几项？"));

n1 = 0
n2 = 1
count = 2

if nterms <= 0:
    print("请输入一个正整数！");
elif nterms == 1:
    print("斐波那契数列");
    print(n1);
else:
    print("斐波那契数列");
    print(n1,",",n2,end=" , ");
    while count < nterms:
        n1,n2 = n2,n1+n2;
        print(n2,end=" , ");
        count += 1;
