# 文件操作

with open("test.txt", "wt") as file:
    file.write("This is a test file!\n Do you see me?");

with open("test.txt", "rt") as file:
    text = file.read();

print(text);    
