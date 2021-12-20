#文件行数f = open("latex.log")
s = 0
for line in f:
    line = line.strip('\n')
    if len(line) == 0:
        continue
    s += 1
print("共{}行".format(s))

# 文件字符分布
f = open("latex.log")
cc = 0
d = {}
for i in range(26):
    d[chr(ord('a')+i)] = 0
for line in f:
    for c in line:
        d[c] = d.get(c, 0) + 1
        cc += 1
print("共{}字符".format(cc), end="")
for i in range(26):
    if d[chr(ord('a')+i)] != 0:
        print(",{}:{}".format(chr(ord('a')+i), d[chr(ord('a')+i)]), end="")

#文件独特行数
# 统计附件文件的小写字母a-z的字符分布，即出现a-z字符的数量，并输出结果。
f = open("latex.log")
ls = f.readlines()
s = set(ls)
for i in s:
    ls.remove(i)
t = set(ls)
print("共{}独特行".format(len(s)-len(t)))

#csv格式转换
f = open("data.csv")
for line in f:
    line = line.strip("\n")
    ls = line.split(",")
    ls = ls[::-1]
    print(",".join(ls))
f.close()

#csv 格式清洗
# 附件是一个CSV文件，其中每个数据前后存在空格，请对其进行清洗，要求如下：
# （1）去掉每个数据前后空格，即数据之间仅用逗号(,)分割；
# （2）清洗后打印输出。
f = open("data.csv")
s = f.read()
s = s.replace(" ","")
print(s)
f.close()