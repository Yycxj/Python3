
def test (a):
    line = a.readline()
    if line :
        print (f"##{line}")
        test (a)
txt = open ('annex/languages.txt')
test (txt)