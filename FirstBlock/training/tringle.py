class TringleChecker():
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c


    def is_triangle(self):
        if self.a +self.b>self.c and self.c +self.b>self.a and self.a +self.c>self.b:
            print('Треугольник возможен!!!')
        elif self.a<0 and self.b<0 and self.c<0:
            print('Треугольник с отриц сторонам невозможен')
        elif self.a +self.b<=self.c or self.c +self.b<=self.a or self.a +self.c<=self.b:
            print('make tringle with such sides is impossible')
        else:
            print('Необходимо вводить только числа!')

tringle1=TringleChecker(a=int(input('the first side is:')),b=int(input('the secong side is:')),c=int(input('the third side is:')))
tringle1.is_triangle()

class TringleChecker1():
    def __init__(self, sides):
        self.sides=sides


    def is_triangle1(self):
        if all(isinstance(side, (int,float)) for side in self.sides):
            if all(side>0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return "you can male tringle"
                return 'you vant make tringle'
            return "Only positive numbers"
        return 'Only numbers!!!'

list_num=[]
list_num.append(int(input('the first:')))
list_num.append(int(input('the secon:')))
list_num.append(int(input('the third:')))
tringle2=TringleChecker1(sides=list_num)
print(tringle2.is_triangle1())



