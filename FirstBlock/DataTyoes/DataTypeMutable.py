#Изменяемые
#Списки
a=[1,5,7,3,7,4,7,7,7,7]
b=list['hello','hello',1,2,3,4]
d=['Hello','Hello']
print(b,'\n\n')
#Словари
dict = {'Name':'Алиса', 'Age':27, 'Job':'Senior Python Developer'}
print(dict,id(dict))
dict['family']='big family'
print(dict,id(dict))
del dict['Age']
print(dict['Name'])
print(dict, '\n\n')
#Множества
e=set(d)
print(e)
c=set(a)
c.add(8)
print(c,'\n\n')