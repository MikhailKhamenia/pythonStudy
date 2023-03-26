def f(x):
    return x * x

def modify_list(L, fn):
    for idx, v in enumerate(L):
        L[idx] = fn(v)

L = [1, 3, 2]
modify_list(L, f)
print(L)

def f1(x):
    return x * x
print(f1(7))

L = [1, 2, 3, 4]
a=list(map(lambda x: x**2, L))
print(a, type(a))


def even_fn(x):
  if x % 2 == 0:
    return True
  return False
print(list(filter(even_fn, [1, 3, 2, 5, 20, 21])))

print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21])))



class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Alex = Employee('Alex', 20)
Amanda = Employee('Amanda', 30)
David = Employee('David', 15)
L = [Alex, Amanda, David]
L.sort(key=lambda x: x.age)
print([item.name for item in L])