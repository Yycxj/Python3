#人民币美元转换
xxx = input()
if xxx [0:3] in ["RMB"] :
    U = eval(xxx[3:]) / 6.78
    print ("USD{:.2f}".format(U))
else :
    R = eval(xxx[3:]) * 6.78
    print ("RMB{:.2f}".format(R))
