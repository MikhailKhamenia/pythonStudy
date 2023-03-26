#Неизменяемые
#Целочисленное
a=3
b=4
print("Целочисленные объекты: ", int(b+a), '\n\n')

#Вещественные
a=3.4
b=4.9
c=a*b
print(c, '\n\n')

#Кортежи
myfirsttuple=(1,2,3, "Я БОГ")
print(myfirsttuple, id(myfirsttuple))
myfirsttuple=("Я БОГ", [1.2,4,6,'trtrtr'])
print(myfirsttuple,id(myfirsttuple))
print(myfirsttuple[::-1])
print(myfirsttuple[::2])
print(myfirsttuple+tuple(['python top', 34,56]), '\n\n')
#Строки
a='I love mam'
b='and dad'
print(a+b,'\n\n')
#fROXENSET
words = ['hello', 'daddy', 'hello', 'mum']
frozen= frozenset(words)
print(frozen,'\n\n')
#Bool тип
a=True
b=False
print (a,b)

