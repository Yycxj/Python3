#四位数玫瑰花数
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                e = a*1000+b*100+c*10+d
                if (pow(a,4)+pow(b,4)+pow(c,4)+pow(d,4))==e:
                    print("{}".format(e))

s = ""
for i in range(1000, 10000):
    t = str(i)
    if pow(eval(t[0]),4) + pow(eval(t[1]),4) + pow(eval(t[2]),4) + pow(eval(t[3]),4) == i :
        print(t)       

#100以内素数和

i = 2
sum = 0
while i < 100:
    for a in range(2,i-1):
        if i%a == 0:
            break
    else:
        sum = sum+i
    i = i+1
print(sum)

sum = 0
for i in range(2,101):
    for j in range(2,i-1):
        if i%j==0:
            break
    else:
        sum = sum + i
print("{}".format(sum))