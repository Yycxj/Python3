#无空隙回声输出
# 描述
# 获得用户输入，去掉其中全部空格，将其他字符按收入顺序打印输出。
num = input()
num = num.replace(' ','')
print(num)


# 文件关键行数
# 描述
# 关键行指一个文件中包含的不重复行。关键行数指一个文件中包含的不重复行的数量。统计附件文件中与关键行的数量。
dict ={}
with open('latex.log','r',encoding='utf-8')as f:
    lines = f.readlines()
    for line in lines:
        rline = line
        dict[rline]=dict.get(rline,0)+1
print('共{:}关键行'.format(len(dict)))

#V2
with open('latex.log','r',encoding='utf-8') as f: #打开文件
    rows_set = set(f.readlines()) # 去除重复行就想到set去重
print('共{}关键行'.format(len(rows_set))) # format标准化输出 len直接取set的长度

#字典翻转输出
# 读入一个字典类型的字符串，反转其中键值对输出。
# 即，读入字典key : value模式，输出value : key模式。
# 用户输入的字典格式的字符串，如果输入不正确，提示：输入错误。

a = input()
try:
    a = eval(a)
    print(dict(zip(a.values(), a.keys())))
except:
    print('输入错误')
#V2
a = input()
try:  # 因为题目要求有输入错误时的输出 就考虑到异常处理
    a = eval(a)
    print(dict(zip(a.values(), a.keys()))) # 直接反向输出
    # 这里有两个函数 zip()  dict() 见下注释
except:
    print('输入错误') # 异常抛出

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

#沉默的羔羊之最多的单词
# 附件是《沉默的羔羊》中文版内容，请读入内容，分词后输出长度大于2且最多的单词。
# 如果存在多个单词出现频率一致，请输出按照Unicode排序后最大的单词。

import jieba

with open('沉默的羔羊.txt','r',encoding='utf-8')as f: # 打开文件
    txt = f.read() # 读取为txt
    words = jieba.lcut(txt) # 利用jieba库的lcut分词
    counts={} # 创建字典
    for word in words: # 逐个遍历
        if len(word) == 1: # 若是当前词语只出现一次 跳过
            continue
        else:
            counts[word]=counts.get(word,0)+1 # 此时词语出现次数累加
list = list(counts.items()) # 字典中items（）方法见下
# 反向排列 key值为字典的[1]索引 = value
list.sort(key=lambda x:x[1],reverse=True) 
print(list[0][0]) # 输出第一
