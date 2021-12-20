# import time
# from typing_extensions import runtime
# pi = 0
# N = 100000
# start = time.perf_counter()

# for k in range(N):
#     pi += 1/pow(16,k) * ( \
#         4/(8*k+1) - 2/(8*k+4) \
#             - 1/(8*k+5) - 1/(8*k+6))

# end = time.perf_counter()
# runtime = end - start
# print (f"圆周率是:{pi}\n程序耗时为{runtime}s")

from random import random, seed
# from time import perf_counter
putin = eval(input())
DARTS = putin 
hits = 0.0
seed(123)
# start = perf_counter()
for i in range(1,DARTS+1):
    x,y = random(),random() # i 点的坐标
    dist = pow(x ** 2 + y ** 2, 0.5) # 计算i点到圆心的距离  （ x^2 + y^2 ）的开平方
    if dist <=1.0:
        hits = hits +1
pi = 4 * (hits/DARTS)
# print (f"圆周率的值是:{pi}")
print ('{:.6f}'.format(pi))
# print ("运行时间是：{:.5f}".format(perf_counter()-start))