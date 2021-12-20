#
#计算文本的平均列数
#
# 打印输出附件文件的平均列数，计算方法如下：
# （1）有效行指包含至少一个字符的行，不计算空行；
# （2）每行的列数为其有效字符数；
# （3）平均列数为有效行的列数平均值，采用四舍五入方式取整数进位。
# f = open("latex.log")
# s, c = 0, 0
# for line in f:
#     line = line.strip("\n")
#     if line == "":
#         continue
#     s += len(line)
#     c += 1
# print(round(s/c))

#csv 格式清洗与转换
# 附件是一个CSV格式文件，提取数据进行如下格式转换：
# （1）按行进行倒序排列；
# （2）每行数据倒序排列；
# （3）使用分号（;）代替逗号（,）分割数据，无空格；
# 按照上述要求转换后将数据输出。
f = open("data.csv")
ls = f.readlines()
ls = ls[::-1]
lt = []
for item in ls:
    item = item.strip("\n")
    item = item.replace(" ", "")
    lt = item.split(",")
    lt = lt[::-1]
    print(";".join(lt))
f.close() 