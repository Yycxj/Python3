#用n的阶乘展示递归
def fact(n):
    if n == 0:
        return 1
    else :
        return n * fact(n-1)

print(fact(5))

#递归方式 翻转字符串
def rvs (s):
    if s == '':
        return s
    else :
        return rvs(s[1:])+s[0]
        
a = "123456"
print(rvs(a))

#递归方式实现斐波那契数列
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else :
        return (f(n-1) + f(n-2))

a = 10
print(f(a))

#递归方式实现汉诺塔问题
count = 0
def hanoi(n,src,dst,mid):
    #  n 个圆盘,从 第 src 第一根 源柱子到 dst 第二根 目标柱子，以 mid 第三根过渡柱子过渡
    global count
    if n == 1:
        print(f"第{1}个圆盘: {src}->{dst}")
        count += 1
    else :
        hanoi(n-1,src,mid,dst) #将n-1个圆盘从第一根 源柱子搬运到第三根柱子
        print(f"第{n}个圆盘: {src}->{dst}")
        count += 1
        hanoi(n-1,mid,dst,src) #将n-1个圆盘从第三根 过渡柱子搬运到第二根目标柱子
x = 3
hanoi(x,'A','B','C')
print (f"总共 {x} 个圆盘，搬运了 {count} 次")