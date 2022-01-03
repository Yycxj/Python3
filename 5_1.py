#函数的定义与使用
#计算n！//m
def fact(n,m=1):
    s=1
    for i in range(1, n+1):
        s = s*i
    return s//m

def fact2 (n, *b):
    s=1
    for i in range(1, n+1):
        s = s*i
    for item in b:
        s = s* item
    return s