


class Soda:
    def __init__(self,name, dobavka):

        print(f'Создание класса {name}')
        if isinstance(dobavka, int):
            self.dobavka=dobavka

    def show_my_drink(self):
        if self.dobavka:
            print(f'Газировка с {self.dobavka}')
        else:
            print('Обычная газироквка')

obj=Soda('содовая', 5)
obj.show_my_drink()

class sodovay(Soda):
    def __init__(self):
        Soda.__init__(self, name='rgeg', dobavka=6)
    def show_my_drink(self):
        print(f'шАЗИРОВУКА С {self.dobavka}')

obj1=sodovay()
obj1.show_my_drink()




