class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    def __set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def __get_kg(self):
        return self.__kg

    kg = property(__get_kg, __set_kg)

obj=KgToPounds(4)
print(obj.to_pounds())


class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')


# Тесты
weight = KgToPounds(12)
print(weight.to_pounds())
print(weight.kg)
weight.kg = 41
print(weight.kg)
weight.kg = 'десять'