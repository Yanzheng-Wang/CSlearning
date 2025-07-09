jimscore = int(input())
jerryscore = int(input())
winner = "jim" if jimscore > jerryscore else "jerry" # 需要加引号，为字符串


print(winner)


def move(n, a, b, c):
    if n==1:
        print(a, "->", c)
        return
    move(n-1, a, c, b)
    move(1, a, b, c)
    move(n-2, b, a, c)

move(3, "a", "b", "c")


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