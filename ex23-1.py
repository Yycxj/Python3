
def test (a):
    line = a.readline()
    if line :
        print (f"##{line}")
        test (a)
txt = open ('languages.txt')
test (txt)