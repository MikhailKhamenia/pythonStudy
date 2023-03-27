class Pet:
    def __init__(self,name=''):
        print('Hi! I’m your new pet! My name is: %s' % name)
        self.name = name
    def feedme(self):
        print('%s says: I’m hungry! Feed me!' % self.name)
    def eat(self,food_name):
        print('%s just ate a %s' %(self.name,food_name))
# Создайте класс Dog, который наследует классу Pet
class Dog(Pet):
    def __init__(self,name=''):
        print('Hi! I’m your new dog!')
        self.name = name
# Протестируйте программу
d = Dog('BaRANKA')
d.feedme()
d.eat('Potato \n\n')


class Parrot(Pet):
    def __init__(self, name):
        print('Hi! I’m your new parrot!')
        self.name = name

    def eat(self, food_name):
        print('% s is pecking at their food!' % (self.name))
        print('% s just ate a % s' % (self.name, food_name))

p=Parrot('Kesha')
p.eat('caarot')