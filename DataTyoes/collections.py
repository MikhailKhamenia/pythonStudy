import collections

#collections.counter
c=collections.Counter()

for element in [(1,2,3),(1,2,3),(1,2,3), 'hello',12,'hello',12,13]:
    c[element] += 1
print(c, '\n\n')

c = collections.Counter(a=4, b=2, c=0, d=-2,e=10)
print(list(c.elements()),'\n\n')

#collections.defaultdict
defdict = collections.defaultdict(list)
print(defdict)
for i in range(5):
    defdict[i].append(i**i)
print(defdict)
defdict=dict(list())
for i in range(10):
    defdict[i]=i*i
print(defdict,'\n\n')

#collections,orderdict
d = {'3':'m3','1':'cayman', '8':'rs4','6':'e43amg'}
print(d)
d=collections.OrderedDict(sorted(d.items(), key=lambda t: t[0]))
print(d)
d=collections.OrderedDict(sorted(d.items(), key=lambda t: t[-1]))
print(d)
d=collections.OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
print(d)
item= d.popitem(True)
print(item)
print(d)
d['mers']=3
d.move_to_end('3')
d.move_to_end('6',False)
print(d)
d.pop('mers')
print(d,type(d), '\n\n')

#collections.namedtuple()
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
print(p)
print(p.x)
print(p[1])