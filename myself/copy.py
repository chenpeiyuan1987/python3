import os;
import sys;

# 读取文件内容
def read(fileName):
  # print("read()");
  fd = os.open(fileName,os.O_RDONLY);
  text = "";
  while True:
    tmp = os.read(fd,1024)
    if len(tmp) == 0:
      break;
    text += tmp.decode();
  os.close(fd);
  return text;

# 内容写入文件
def write(fileName, text):
  # print("write()");
  fd = os.open(fileName,os.O_WRONLY|os.O_CREAT);
  os.write(fd,text);
  os.close(fd);

# 主函数
def main(args):
  if len(args) == 1:
    print("\n缺少参数");
  elif len(args) == 2:
    text = read(args[1]);
    print(text);
    print("\n读取完毕");
  elif len(args) == 3:
    text = read(args[1]);
    write(args[2],text.encode());
    print("\n复制完毕");

main(sys.argv);
