# # template = "零一二三四五六七八九"
# template = ['零','一','二','三','四','五','六','七','八','九']
# s = input()
# for c in s:
#     # print (eval(c))
#     print(template[eval(c)])

list = ['零','一','二','三','四','五','六','七','八','九']
x = input()
for c in x:
    print (list[eval(c)],end='')