import sys
script,encoding,error = sys.argv


def main (language_file,encoding,errors):
    line = language_file.readline()
    
    if line:
        print_line (line,encoding,errors)
        return main (language_file,encoding,errors)
            
            
def print_line (line,encoding,errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding,errors = errors)
    #把字符串变成字节
    cooked_string = raw_bytes.decode(encoding,errors = errors)
    #把字节变成字符串
    # contrast.write(raw_bytes)
    print (raw_bytes, "<===>", cooked_string)
    
    
languages = open ("annex/languages.txt", encoding = "utf-8")
# contrast = open ("contrast","a")
main (languages,encoding,error)