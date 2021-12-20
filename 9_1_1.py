#系统基本信息获取

import sys
s1=sys.getrecursionlimit()
s2=sys.executable
s3=sys.maxunicode
print("RECLIMIT:{}, EXEPATH:{}, UNICODE:{}".format(s1,s2,s3))

# import sys
# print("RECLIMIT:{}, EXEPATH:{}, UNICODE:{}".format(sys.getrecursionlimit(), sys.executable, sys.maxunicode))

#二维表格输出
from tabulate import tabulate
data = [ ["北京理工大学", "985", 2000], \
         ["清华大学", "985", 3000], \
         ["大连理工大学", "985", 4000], \
         ["深圳大学", "211", 2000], \
         ["沈阳大学", "省本", 2000], \
    ]
print(tabulate(data, tablefmt='grid'))