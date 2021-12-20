#计算水仙花数

list1 = []
for x in range(100,1000):
    a = x//100
    b = x%100//10
    c = x%100%10
    # print (a,b,c)
    if pow(a,3)+pow(b,3)+pow(c,3) == x:
        list1.append(x)
    else:
        continue
for i in list1:
    if i == list1[-1]:
        print (i)
    else:
        print(i,end=',')
# s = ""
# for i in range(100, 1000):
#     t = str(i)
#     if pow(eval(t[0]),3) + pow(eval(t[1]),3) + pow(eval(t[2]),3) == i :
#         s += "{},".format(i)
# print(s[:-1])
