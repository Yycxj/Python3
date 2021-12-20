#开平方
a = input()
a = eval(a)
x = pow(a,0.5)
print("{:+>30.3f}".format(x))

#分割
a = input()
a = a.split('-')
print (f"{a[0]}+{a[-1]}")

#倒序输出
a = 'Alice+Flurry'
print (a[::-1])

k = 10000
a= 0
while k>1:
    k = k/2
    a = a+1
print(a)