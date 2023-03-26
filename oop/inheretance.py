# app.py

class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is Student
    def isStudent(self):
        return True


# Inherited or Subclass(Note Person in bracket)
class Student(Person):

    # Here we return true
    def isStudent(self):
        return False


# Driver code
person = Person("Eleven")  # An Object of Person
print(person.getName(), person.isStudent())

student = Student("Krunal")  # An Object of Student
print(student.getName(), student.isStudent(), '\n\n')

class GrandParents(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name


# Inherited or SubClass
class Parents(GrandParents):

    # Constructor
    def __init__(self, name, age):
        GrandParents.__init__(self, name)
        self.age = age

    # To get name
    def getAge(self):
        return self.age


# Inherited or SubClass
class Children(Parents):

    # Constructor
    def __init__(self, name, age, address):
        Parents.__init__(self, name, age)
        self.address = address

    # To get address
    def getAddress(self):
        return self.address

g = Parents("Krunal", 360001)
print(g.getName(), g.getAge())
# Driver code
g = Children("Krunal", 360001, "Rajkot")
print(g.getName(), g.getAge(), g.getAddress(),'\n\n')

# app.py

class Base1(object):
    def __init__(self):
        self.str1 = "Eleven"
        print("First Base Class")


class Base2(object):
    def __init__(self):
        self.str2 = "Krunal"
        print("Second Base Class")


class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived Class")

    def printData(self):
        print(self.str1, self.str2)


obj = Derived()
obj.printData()


