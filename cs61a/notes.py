print('PART 1')

#   assert boolean context(true) ,'...'
# 1.using python -0 ,the terminal will omit assert
# 2.check some circumstance that shouldn't occur
# subex1 and subex2 is euqal to subex1 && subex2 in cpp
# subex1 or subex2 is euqal to subex1 || subex2 in cpp

def area(r, shape_constant):
    """
    >>> area(1, 1)
    1
    >>> area(2, 2)
    8
    """
    assert r > 0, 'radius must be positive'
    return r**2 * shape_constant

def area_square(r):
    return area(r,1)


# from inspect import trace
from math import pi,sqrt

def area_circle(r):
    return area(r,pi)

def area_hexagon(r):
    return area(r,3*sqrt(3)/2)

# python -m doctest name.py can test the code
# if terminal out nothing, it means all the test passed

# python -m doctest -v name.py can test the code
# if terminal out the annotation, it means all the test passed    # doctest: +SKIP




















print('PART 2')

# higher order functions
# Functions can be manipulated as values in our programming language ,such as following term
# A function that  takes a function as an argument value or return a function as a return value

# general version of summation
# take a function as an argument

def summation(n,term):
    total,k=0,1
    while k<=n:
        total,k = total + term(k) , k + 1
    return total

def identity(k):
    return k

def cube(k):
    return pow(k,3)

from operator import mul 

def pi_term(k):
    return 8 / mul(4 * k -3, 4 * k -1) 

def sum_natural(n):
    return summation(n,identity)

def sum_cube(n):
    """sum the first N cubes of natural numbers"""
    return summation(n,cube)

def sum_topi(n):
    return summation(n,pi_term)

# function as return values

def make_adder(n):
    """
    return a function that takes one argument K and return K + N

    #10 is n and 1 is k;
    >>> make_adder(10)(1)  # 10是n，1是k
    11     
                                
    >>> f=make_adder(1)
    >>> f(1)
    2
    """
    def adder(k):
        return n+k
    return adder
#make_adder(10)is the operator and 1 is the opearand

# another example

def counter():
    count = 0
    def increment():
        nonlocal count  # 声明使用外层变量
        count += 1
        return count
    return increment

c = counter()               #c被赋值为increment(),执行c()并不会重新初始化count
print(c())  # 1             #increment引用了外层变量count,每次调用c()使用的都是closure里保存的count
print(c())  # 2
print(c())  # 3

c1 = counter()  # 闭包1：count=0
c2 = counter()  # 闭包2：count=0（与闭包1无关）

print(c1())  # 1（修改闭包1的count）
print(c1())  # 2
print(c2())  # 1（修改闭包2的count）

# def counter_broken():
#     count = 0
#     def increment():
#         count += 1  # 报错：UnboundLocalError（没有nonlocal声明）
#         return count
#     return increment

# c = counter_broken()
# c()




















print('PART 3')

"""Recursion"""

# self-reference

def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x+y)
    return next_sum

"""
>>> print_sums(1)(3)(5)
1
4
9

"""
#1,3,5依次传入，每次返回函数接受下一个参数

# recursive function 

def split(n):
    return n // 10, n % 10

def sum_digits_rec(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits_rec(all_but_last) + last

print(sum_digits_rec(123456789))

# iteration is a special case of recursion

def sum_digits_iter(n):
    digit_sum = 0
    while n>0:
        n, last = split(n)
        digit_sum += last
    return digit_sum

# mutual recursion

def luhn_sum(n):
    if n < 10:
        return n 
    else:
        all_but_last , last = split(n)
        return luhn_sum_double(all_but_last)+ last

def luhn_sum_double(n):
    all_but_last , last= split(n)
    luhn_digit = sum_digits_rec(last*2)
    if n<10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last)+ luhn_digit

# def luhn_sum(n, k=1):                   #using argument k to control the recursion
#     def luhn(n):
#         if n * 2 < 10:
#             return n * 2
#         else:
#             return n * 2 // 10 + n * 2 % 10

#     if n == 0:
#         return 0
#     else:
#         all_but_last, last = split(n)
#         if k % 2 == 0:
#             return luhn_sum(all_but_last, k + 1) + luhn(last)           #when using the function, k will be incremented
#         else:
#             return luhn_sum(all_but_last, k + 1) + last

# Example usage
print(luhn_sum(123456789))  # This should print the Luhn sum of 123456789





















print("PART  4")

"""Functional Abstraction"""

# lambda argument: expression
"""
lambda x: x**2 
is equal to 
def square(x):
    return x**2

    decorator
    @decorator
    def fuc()
        ...                         #运行后直接显示函数名

    decorator(lambda x:x**2)(2)     #运行后显示<lambda>


lambda in closure unlike other func can use nonlocal to change the value of variable.
lambda can't.
    """
# lambda will return the value of the expression

a = 1
def f(g):
    a = 2
    return lambda y: a*g(y)
print(f(lambda y: a+y)(a))

# return: switch back to the previous environment
# return can terminal an infinite loop
# !!!!!!!!!!!!!!!!!confused!!!!!!!!!!

def search(f):
    x = 0
    while True:
        x += 1
        if f(x):
            return x
        
def inverse(f):
    '''Return g(y) such that g(f(x)) -> x.'''
    return lambda y: search (lambda x : f(x) == y)

def square(x):
    return x*x


"""Function Examples"""

#

def delay(arg):
    """_summary_

    Args:
        arg (_type_): _description_

    Returns:
        _type_: _description_
    """
    print('dealyed')
    def g():
        return arg
    return g

delay(delay)()(6)()            # 从内到外

# implementing functions

def remove(n, digit):
    """_summary_

    Args:
        n (_type_): _description_
        digit (_type_): _description_

    Returns:
        _type_: _description_
    """
    kept, digits = 0, 0
    while n > 0:
        n, last = n//10, n%10
        if last != digit:
            digits = digits + last*10**kept
            kept = kept + 1 
    return digits

def split(n):
    return n//10, n%10

def num_eights_in_a_row(n):
    # judge = False
    # # while n > 0:
    # #     n, last0 = split(n)
    # #     all_but_last, last1= split(n)
    # #     if last0 == last1 and last0 ==8:
    # #         judge = True
    # # return judge
    # i = 0
    # while n > 0:
    #     n, last = split(n)
    #     if last == 8:
    #         all_but_last, last = split(n)
    #         if last == 8:
    #             judge = True
    # return judge
    count = 0
    nums = 0
    while n >0:
        last = n%10
        if last == 8:
            count+=1
        else :
            if count >= nums:
                nums =count
            count = 0
        n //= 10
    if nums == 0:
        nums =count
    return nums


"""         decorator

    @trace
    def triple(x):
        return 3*x

    is identical to 

    def triple(x):
        return 3*x
    triple = trace(triple)

"""

# from skywalking.trace import trace


def trace1(fn):
    def traced(x):
        print('calling', fn.__name__, 'on argument', x )
        return fn(x)
    return traced


# @trace1
def square(x):
    return x*x

square = trace1(square)

@trace1
def sum_square_up_to(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + square(k), k + 1
    return total

















print("PART    5")

"""
 Tree Recursion
"""

# Order of Recursive Calls

def cascade(n):
    """
    >>> cascade(123)
    123
    12
    1
    12
    123
    """
    if n < 10:
        print(n)
    else :
        print(n)
        cascade(n//10)
        print(n)
    """
    print(n)
    if n >10:
        cascade(n//10)
        print(n)
    """

def inverse_cascade_onmyown(n):
    k = 0
    flag = True
    while flag:
        if n // 10**(k+1) == 0:
            flag = False
        else:
            k +=1
    n = n / 10**k               # Convert n into a decimal so that it can be used to output 
                                # from the lower digit to the higher digit with round later on.
    def inter(n):
        print(round(n))
        if n <= 10**k:
            inter(n * 10)
            print(round(n))
    return inter(n)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

inverse_cascade(12345)


# Tree recursion 

# Tree_shaped processes arise whenever executing the body of a 
# recursive function makes more than one call to that function.
        
def fib(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else :
        return fib(n-1) + fib(n-2)
    

# !!!!!!!example : Count Partitions

def count_partitions_onmyown(n, m):
    if n <= 0 or m == 0 :
        return 0
    elif m == 1:
        return 1
    elif m >= n:
        return 1 + count_partitions_onmyown(n, n-1)    # its effect is equal to teacher's if n ==0:return 1
    # elif m > n:                                   unpracticable
    #     return count_partitions_onmyown(n, n)
    else :
        return count_partitions_onmyown(n-m, m) + count_partitions_onmyown(n, m-1)

# count_partitions(6,4)
# explore two possibilities:1.use at least one 4 
#                           2.don't use any 4
# solve two simpler problems:1.count_partitions(2,4)
#                            2.count_partitions(6,3)

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else :
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m
    

























print("PART    6")

"""Sequences"""

# list 

# 1. list = [1, 2, 3]
# 2. the element of list aren't just integer ,but can be everything including nested list
list1 = [1, 'fd', [323,33]]

# 3. the number of elements --------len(list)
print(len(list1))

# 4. an element selected by its index
# list[1] == getitem (list, 1)
from operator import getitem
print(list1[2])
print(getitem(list1, 2))

# 5. Concatenation and Repetition
list2 = [2,4] + list1*2         # is euqal to add(list2, mul(list1, 2))
print(list2)

# Containers
# (element in list) will output a bool ,like logic operator
print(1 in list1)
# True

print('1' in list1)
# False

# it doesn't look for subsequence ,but individual element
print([1, 'fd'] in list1)
# False

print([1, 2] in [[1,2], 23, 3])
# True

print([1, 2] in [[[1,2]], 3, 3])
#　False

# For statement
# for <name> in <expression>:
#     <suite>(indented)

def count_value(s, value):
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

# sequence unpacking
same_count = 0
for x, y in [[1, 3], [3, 3], [2, 2], [1, 5]]:   # looks like multiple assignment
    if x == y:
        same_count += 1
print(same_count)

# Ranges
# a range is a sequence of consecutive integers(include the starting value and exclude the ending value)
# length is the ending value minus the starting value
# element selection --- starting value plus index(from 0)

print(range(-1, 4))
# range(-1, 4)

print(list(range(-1, 4)))
# [-1, 0, 1, 2, 3]

"""
>>> list(range(3))                  #implicit starting value is 0
[0, 1, 2]
>>> list(range(-4,0))
[-4, -3, -2, -1]
>>> list(range(-4))         #   __________
[]
"""

def cheers():
    for _ in range(3):
        print('Go Bears')
    
# List Comprehension
# [<expression> for element in sequence (if bool)]

odds = [1, 3, 5, 7, 9]
list3 = [x+1 for x in odds if 25 % x == 0]
print(list3)

def divisors(n):
    return [1] + [x for x in range(2, n) if n%x == 0]

# List ,Slice & Recursion 
# list[?:?:?]

print(list1[1:])

def sum_list(s):
    if len(s) == 0:
        return 0
    else :
        return s[0] + sum_list(s[1:])

# ！！！！！！！！！！！！！！！！！！entail tree recursion

"""
def large(s, n):
    Return the sublist of positive numbers s 
    with the largest sum that is less than or equal to n
>>> large([4, 2, 5, 6, 7], 3)
[2]
>>> large([4, 2, 5, 6, 7], 3)
[2, 6]
>>> large([4, 2, 5, 6, 7], 3)
[4, 2, 6, 7]
>>> large([4, 2, 5, 6, 7], 20)
[2, 5, 6, 7]
    """

def large(s, n):
    if s == []:
        return []
    elif s[0] > n:
        return large(s[1:], n)
    else :
        with_s0 = [s[0]] + large(s[1:], n-s[0])
        without_s0 = large(s[1:], n)
        if sum_list(with_s0) >= sum_list(without_s0):
            return with_s0
        else:
            return without_s0