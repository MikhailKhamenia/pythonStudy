class SomeClass:
    def __private(self):
        print("Это внутренний метод объекта")

obj = SomeClass()

#obj.__private() #нельзя, так как это приватный метод
obj._SomeClass__private() #обход для вызова приватного метода

class SomeClass():
    def __init__(self, value):
        self._value = value

    def getvalue(self): # получение значения атрибута
        return self._value

    def setvalue(self, value): # установка значения атрибута
        self._value = value

    def delvalue(self): # удаление атрибута
        del self._value

    value = property(getvalue, setvalue,delvalue, "Свойство value")

obj = SomeClass(42)
print(obj.value)
obj.value = 43
print(obj.value, '\n\n')

#Вместо того чтобы вручную создавать геттеры и сеттеры для каждого атрибута,
# можно перегрузить встроенные методы __getattr__, __setattr__ и __delattr__.
# Например, так можно перехватить обращение к свойствам и методам, которых в объекте не существует:
class SomeClass1():
    attr1 = 42

    def __getattr__(self, attr):
        return attr.upper()

obj = SomeClass1()
print(obj.attr1)
print(obj.lkjhgfhds, '\n\n')


#__getattribute__ перехватывает все обращения (в том числе и к существующим атрибутам):
class SomeClass():
    attr1 = 42

    def __getattribute__(self, attr):
        return attr.upper()

obj = SomeClass()
print(obj.attr1) # ATTR1
print(obj.attr2)