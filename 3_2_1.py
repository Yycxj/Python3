#dayday up
# dayup = pow(1.001,365)
# daydown = pow(0.999,365)
# print (f"dayup{dayup},\ndaydown{daydown}")

# dayfactor = 0.005
# dayup = pow(1+dayfactop,365)
# daydown = pow(1-dayfactop,365)
# print (f"dayup{dayup},\ndaydown{daydown}")

# #dayday up Q3
dayfactor = 0.01
day = 1
for i in range(365):
    if (i+1) %7==0 or i%7==0:
        # day = pow(1-dayfactor,2)
        day = day * (1-dayfactor)
    else:
        day = day * (1+dayfactor)
print (f"day{day}")
#dayday op Q3_1
dayfactor = 0.01
dayup = 1
for i in range (365):
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)
print (f"dayup{dayup}")

def dayUP (df):
    dayup = 1
    for i in range (365):
        if i % 7 in [6,0]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*( 1 + df)
    return dayup
dayfactor = 0.01
dayupa = 1
for i in range(365):
    dayupa = dayupa*(1+dayfactor)
while dayUP(dayfactor) < dayupa :
    dayfactor += 0.001
print (f"dayfactor  {dayfactor * 100}%")