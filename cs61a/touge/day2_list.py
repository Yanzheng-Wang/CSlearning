"""
    Python函数参数
     位置参数
     关键字参数 
     默认参数 
     位置可变参数 *args tuple
     关键字可变参数（**kwargs dict
     解包参数 *list,**dict
"""
def plus(a,b,c):
    return a+b+c
list = [1,2,3]
print(plus(*list))

"""
    Iterable  可迭代对象
    Iterator  迭代器
    isinstance([],Iterable) == True
    isinstance([],Iterator) == False
    isinstance(iter([]),Iterable) == True
    iterlist = iter([])
    listnum = next(iterlist)

"""