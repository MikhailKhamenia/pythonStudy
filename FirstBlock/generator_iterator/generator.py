def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print(item)


def gen_func():
    for i in range(100):
        if i > 1:
            for n in range(2, i):
                if (i % n) == 0:
                    break
                yield i
l=[]
for item in gen_func():
    l.append(str(item))
a=[]
for item in l:
    if item not in a:
        a.append(item)

print(' '.join(a), end='')



