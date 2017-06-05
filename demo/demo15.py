# 输出指定范围内的质数

lower = int(input("请输入范围下限："));
upper = int(input("请输入范围上限："));

for num in range(lower, upper+1):
    if (num <= 1):
        continue;

    for i in range(2, num):
        if(num % i == 0):
            break;
    else:
        print(num);
