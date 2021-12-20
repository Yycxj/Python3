#英文字符的鲁棒输入
# 获得用户的任何可能输入，将其中的英文字符进行打印输出，程序不出现错误

# s=input()
# for i in s:
#     if((i>='A' and i<='Z') or (i>='a' and i<='z')):
#         print(i,end='')

#数字的鲁棒输入
# 获得用户输入的一个数字，可能是浮点数或复数，如果是整数仅接收十进制形式，且只能是数字。对输入数字进行平方运算，输出结果。
s=input()
try:
    if(complex(s)==complex(eval(s))):
        print(complex(s))
        print('>>>',complex(eval(s)))
        print(eval(s)**2)
except:
    print("输入有误")