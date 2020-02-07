def dogs_and_cats(amount_of_dogs, amount_of_cats):
    print "I want to raise %d dogs." % amount_of_dogs
    print "I also want to raise %d cats." % amount_of_cats
    print "This is definitely fun.\n"
#第一种：
print "case one: "
dogs_and_cats(5, 6)

#第二种：
print "case two:"
dogs_num = 10
cats_num = 10
dogs_and_cats(dogs_num, cats_num)

#第三种：
print "case three:"
dogs_and_cats(10+10,2+4)

#第四种：
print "case four:"
dogs_and_cats(dogs_num+2,cats_num+3)

#第五种：
print "case five:"
dogs = int(raw_input("please input numbers of dog:"))
cats = int(raw_input("please input numbers of cat:"))
dogs_and_cats(dogs, cats)

#第六种：
print "case six:"
dogs_and_cats(dogs + dogs_num, cats + cats_num)

#第七种：
print "case seven:"
dogs_and_cats(dogs + 12, cats + 3)

#第八种：
print "case eight:"
dogs_and_cats(int(raw_input("dogs:")),int(raw_input("cats:")))

#第九种：
print "case nine:"
dogs_and_cats(int(raw_input("dogs:"))+dogs,int(raw_input("cats:"))+cats)

#第十种：
print "case nine:"
dogs_and_cats(int(raw_input("dogs:"))+3,int(raw_input("cats:"))+4)