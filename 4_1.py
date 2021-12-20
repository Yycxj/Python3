#计算从1加到966
s = 0
for i in range (1,967):
    if i%2 == 0:
        s = s-i
    elif i%2 != 0:
        s = s+i
print (s)

s = 0
count = 1
while count <=966:
    if count%2 == 0:
        s -= count
    else:
        s += count
    count += 1
print(s)