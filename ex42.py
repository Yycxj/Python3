##Animal is-a object (yes, sort of confusing)
class Animal (object):
    pass

##dog is-a 
class Dog (Animal):

    def __init__(self,name):
        ##has-a name 
        self.name = name

## cat is-a animal
class Cat (Animal):

    def __init__(self,name):
        ## animal has-a name
        self.name = name

##Person is-a object
class Person (object):

    def __init__(self,name):
        ##Person has-a name
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

##Employee is-a Person
class Employee(Person):

    def __init__(self,name,salary):
        ##?? hmm what is this strange magic?
        ##子类调用父类时候使用 super（子类名，self）.方法名（参数）
        ##子类 Employee 要调用 父类Person 的 name，以为这里没有name这个东西
        super(Employee,self).__init__(name)
        ##Employee has-a salary
        self.salary = salary

## fish is-a object
class Fish(object):
    pass

## salmon is-a fish
class Salmon(Fish):
    pass

## halibut is-a fish
class Halibut(Fish):
    pass


##rover is-a dog
rover = Dog("Rover")

##satan is-a cat
satan = Cat("Satan")

##mary is-a person
mary = Person("Mary")

##mary has-a pet name is satan
mary.pet = satan

## frank is-a employee, has-a frank salary = 120000
frank = Employee("Frank", 120000)
print (frank.name)
print (frank.salary)

## frank has-a pet, name is rover
frank.pet =rover

##
flipper = Fish()


##
crouse = Salmon()

##
harry = Halibut()
