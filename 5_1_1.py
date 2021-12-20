# def f(a,b):
#     a = 4
#     return a+b
# def main():
#     a=5
#     b=6
#     print(f(a,b),a+b)
# main()

# def func(a,b):
#     c = a**2+b
#     b=a
#     return c
# a=10
# b=100
# c =func(a,b)+a
# print(c)

#随机密码生成
# import random

# def genpwd(length):
#     a = 10**(length-1)
#     b = 10**length - 1
#     return "{}".format(random.randint(a, b))

# length = eval(input())
# random.seed(17)
# for i in range(3):
#     print(genpwd(length))

#连续质数计算
def prime(m):
    for i in range(2,m):
        if m % i == 0:
            return False
    return True

n = eval(input())
n_ = int(n)
n_ = n_+1 if n_ < n else n_
count = 5

while count > 0:
    if prime(n_):
        if count > 1:
            print(n_, end=",")
        else:
            print(n_, end="")
        count -= 1 
    n_ += 1