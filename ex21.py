def add (a,b):
    print (f"ADDING {a} + {b}")
    return a+b

def subtract (a,b):
    print (f"SUBTRACTING {a} - {b}")
    return a-b
    
def multiply (a,b):
    print (f"MULTIPLYING {a} * {b}")
    return a*b

def divide (a,b):
    print (f"DIVIDING {a} / {b}")
    return a/b


print ("Let's do some math with just functi!")

age = add(30,5)
height = subtract (78,4)
weight = multiply (90,2)
iq = divide (100,2)

print (f"Age: {age}, Height: {height},Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print ("Here is a puzzle.")

what = add(age, subtract(height,multiply(weight, divide(iq,2))))
x = (35+(74-(180*(50/2))))

print ("That becomes:",what,"Can you do it by hand")
print (x)

x = (50/2*180-74+35)
this = add(subtract(multiply(divide(iq,2),weight),height),age)
print (x)
print (this)

this = subtract(add(24,divide(34,100)),1023)
x = 24+34/100-1023
print (x)
print (this)