class MetaClass(type):
    # выделение памяти для класса
    def __new__(cls, name, bases, dict):
        print("Создание нового класса {}".format(name))
        return type.__new__(cls, name, bases, dict)

    # инициализация класса
    def __init__(cls, name, bases, dict):
        print("Инициализация нового класса {}".format(name))
        return super(MetaClass, cls).__init__(name, bases, dict)

# порождение класса на основе метакласса
SomeClass = MetaClass("SomeClass", (), {})

class Child(SomeClass):
    def __init__(self, param):
        print(param)

# получение экземпляра класса
obj = Child("Hello\n\n")



class VerboseMetaclass(type):

    def __new__(cls, class_name, class_parents, class_dict):
        print("Creating class ", class_name)
        new_class = super().__new__(cls, class_name, class_parents, class_dict)
        return new_class

class Spam(metaclass=VerboseMetaclass):
    def eggs(self):
        print("[insert example string here]")
s = Spam()
s.eggs()