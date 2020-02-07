def translate (file,coding):
    line = file.readline()
    if line :
        xline = line.strip()
        deline = xline.decode (encoding=coding)
        print (deline)
        translate (file,coding)
        
x = open("contrast.txt")
translate (x,'utf-8')