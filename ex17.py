from sys import argv 
from os.path import exists

script, from_file, to_file =argv

print (f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print (f"The input file is {len(indata)} byt long")
input('>really?')

print (f"Does the output file exist? {exists(to_file)}")
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input('>really?')

out_file = open(to_file,'w')
out_file.write(indata)

print ("Alright, all done.")

out_file.close()
print ("This is file content:\n",open(to_file).read())
out_file.close()
in_file.close()

#All code reduced to one line of code
open('test-1.txt','w').write(open ('test.txt').read())
