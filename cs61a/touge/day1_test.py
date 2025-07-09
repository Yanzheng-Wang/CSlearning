source_string = "  I am a string.  "
print(source_string)
print(source_string.strip())       # 相当于新建了一个字符串
print(source_string.lstrip())
print(source_string)
source_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(source_list)
print(source_list.append(11))      # 相当于取地址或者引用，即在原来的上面改变，返回None
print(source_list)

print(range(10))

keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(dict(zip(keys, values)))
print(dict(a=1, b=2, c=3))
print(zip(keys, values))
my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)

menu_dict = {'a': 1, 'b': 2, 'c': 3}
# for k,v in menu_dict.keys(),menu_dict.values():  # wrong!!不能同时遍历keys()和values()两个独立迭代器
for k, v in zip(menu_dict.keys(), menu_dict.values()):
# for k, v in menu_dict.items():
    print(k)
    print(v)

import collections
print(collections.namedtuple('Point', 'x y'))
Point = collections.namedtuple('Point', 'x y')
p = Point(1, 2)
print(p.x)
print(p)
print(p._asdict())
print(p._replace(x=10))               # 相当于新建一个对象
print(p)
print(type(p))

c = collections.Counter('abracadabra')
print(c)
print(c.subtract('abr'))
c.subtract('aaa')                     # 相当于取地址和引用，即在原来的上面改变，返回None
print(c)
print(type(c))
print(c.most_common())

# deque
# append(),pop(),appendleft(),popleft()
# extend(),extendleft()
print(collections.deque('abcdefg'))
a = collections.deque('abcdefg')
a.append('hsss')
print(a)

data = [('a',1),('b',3),('c',2)]
print(collections.OrderedDict(sorted(data,key=lambda t:t[1])))
print(collections.OrderedDict(sorted(data,key=lambda t:t[1],reverse=True)))
print(sorted(data,key=lambda t:t[1],reverse=True))
dt = collections.OrderedDict(data)
dt.move_to_end('a',last=True)
print(dt)

dd  = collections.defaultdict(list)
print(dd["s"])
print(dd)
print(collections.defaultdict(list,{'a':1,'b':2}))