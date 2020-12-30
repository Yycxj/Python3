from sys import argv

script,filename = argv

txt = open(filename)

print (f"Here's your file {filename}")
print (txt.read())

print ("Type the filename again:")
file_again = input('>> ')

txt_again = open (file_again)

print (txt_again.read())

f = open ('test.py','r+')
data = f.read()
print (data)
f.write ('write1')
print (data)
f.close()
f = open ('test.py','r+')
data = f.read()
print (data)