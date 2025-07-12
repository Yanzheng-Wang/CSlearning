# jimscore = int(input())
# jerryscore = int(input())
# winner = "jim" if jimscore > jerryscore else "jerry" # 需要加引号，为字符串


# print(winner)


# def move(n, a, b, c):
#     if n==1:
#         print(a, "->", c)
#         return
#     move(n-1, a, c, b)
#     move(1, a, b, c)
#     move(n-2, b, a, c)

# move(3, "a", "b", "c")


# 辗转相除法

def gcd(x,y):
    # return x if y==0 else gcd(y,x%y)
    if y == 0:
        return x
    i = y
    while y!=0:
        y = x%y
        x = i
        i = y
    return x

from functools import reduce

r = reduce(lambda x,y : x+y,[1,2,3,4,5])
print(r)

import math

class Solution():
    def get_lcm(self, x):
        # 请在此添加代码，实现求出给定的所有正整数的最小公倍数，并将其返回
        #********** Begin *********#
        if not x:
            return 0
        lcm = x[0]
        for num in x[1:]:
            if num == 0:
                return 0
            gcd = math.gcd(lcm, num)
            lcm = (lcm * num) // gcd
        return lcm
        #********** End **********#