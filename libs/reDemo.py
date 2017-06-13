# re 正则表达式

import re;

# 测试1 
str = "www.runoob.com";
print("测试1",str);
print("1. www - ", re.match("www", str,));
print("2. com - ", re.match("com", str,));

# 测试2
str = "Cats are smarter than dogs";
print("测试2",str);
match = re.match(r"(.*) are (.*?) .*", str, re.M|re.I);
if(match):
    print("match.group():", match.group());
    print("match.group(1):", match.group(1));
    print("match.group(2):", match.group(2));
else:
    print("No match!");

# 测试3
str = "www.runoob.com";
print("测试3",str);
print("1. www - ", re.search("www", str,).span());
print("2. com - ", re.search("com", str,).span());

# 测试4
str = "Cats are smarter than dogs";
print("测试4",str);
match = re.match(r"dogs", str, re.M|re.I);
if(match):
    print("match.group():", match.group());
else:
    print("No match!");

match = re.search(r"dogs", str, re.M|re.I);
if(match):
    print("match.group():", match.group());
else:
    print("No match!");

# 测试5
str = "2004-959-559 # 这是一个电话号码";
print("测试5",str);
num = re.sub(r"#.*$", "", str);
print("电话号码：",num);

num = re.sub(r"\D", "", str);
print("电话号码", num);

