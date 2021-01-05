from sys import argv

script,input_file = argv

def print_all (f):
    print (f.read())
    #输出全部
    
def rewind(f):
    f.seek(0,0)
    #把文件读写位置回档
    
def print_a_line (line_count,f):
    print (line_count , f.readline())
    #单行输出
current_file = open (input_file)
#打开文件

print ("First let's print the whole file:\n")

print_all (current_file)

print ("Now let's rewind, kind of like a tape.")

rewind (current_file)

print ("Let's print three lines:")

current_line = 1
print_a_line (current_line,current_file)

current_line += 1
print_a_line (current_line, current_file)

current_line += 1
print_a_line (current_line, current_file)
# current_line = current_line +1
# print_a_line (current_line, current_file)
# current_line = current_line +1
# print_a_line (current_line, current_file)
# current_line = current_line +1
# print_a_line (current_line, current_file)
# current_line = current_line +1
# print_a_line (current_line, current_file)
# current_line = current_line +1
# print_a_line (current_line, current_file)
# current_line = current_line +1
# print ("?")
# rewind (current_file)
# print_a_line (current_line, current_file)
# # current_line = current_line +1
# print_a_line (current_line, current_file)
# # current_line = current_line +1
# print_a_line (current_line, current_file)
# # current_line = current_line +1
# print_a_line (current_line, current_file)
# # current_line = current_line +1

