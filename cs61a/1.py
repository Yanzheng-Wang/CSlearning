# a = 1
# b = 2

# c = a/b
# print(c, a, b)

# a = [1, 2, 3, 4]

# for i in a:
#     print(i)

from xml.etree.ElementTree import tostring


nums = [5, 1, 4, 3, 2]
# length = 0
# for i in nums:
#     length += 1

# for i in range(length -2):
#     for j in range(length - i -1):
#         if nums[j]>nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
# print(nums)

print(nums[1:3])

str1 = '秦杰帅吗？'
str2 = '\n帅死了！！！'
print(str1 +str2)  #拼接字符串和列表
# print(tostring(nums)+str1)

num = [1]
print(num * 10)    #生成重复的字符串和列表
# print(num ** 10) #wrong

print(len(nums), len(str1))
a = '1'*10
print(a.count('1'))  #统计数量

nums = [1, 2, 3, 4, 5, 6]
print(nums[0::2])
print(nums[::-1])

a = 2
print(f"{a:03d}123")

a = r"C:\Users\86186\Desktop\CSlearning\cs61a\1.py"   #windows 一定要加r
print(a.split('\\'))
# print(nums.join('s'))   #'list' object has no attribute 'join'

numss = [1, 2, 3, 4, 5, 6]
numss.append(22) #结尾接入
print(numss)
numss.insert(0,7) #插入
print(numss)

a = [1, 2, 3, 4]
b = a.pop()         #列表数据弹出
c = a.pop(1)
print(a, b, c)

nums = [5, 3, 2, 1, 4]
# nums.sort()
nums.sort(reverse = True) #从小到大 默认False
print(nums)

strs = ['aaaa', 'aaa', 'aa', 'a']
strs.sort(key = lambda x:len(x))
print(strs)
print(strs.index('aa'))

dic = {1:"秦杰",
       2:"真的帅",
       "sss":'sdfas'}
dic[3] = '真的帅的没边了'
dic.pop('sss')  #字典数据弹出
b = dic.get(4,'你难道不这么认为？') #同上
print(dic[1]+dic[2]+'\n'+dic[3])
print(dic.keys(), dic.values())
print(b)

dic_new = {1:"秋雨"}
dic.update(dic_new)
print(dic)

nums = [1, 1, 2, 3, 3 ,3 ,5 ,6, 4]
nums = ["a"] + nums
i ,j = 0, 1
length = len(nums)
while j < length-1:
    if nums[j] == nums[j+1]:
        j += 1
    elif j - i > 1:
        for k in range(i+1,j+1):
            nums.pop(k)
        j = i + 1
        length = len(nums)
    else:
        i += 1
        j += 1
print(nums[1:])
# dic1 = {}
# for i in nums:
#     if not (i in dic1.keys()):
#         dic1[i] = 1
#     else:
#         dic1[i]+=1
# print(dic1)
# nums = []
# for key in dic1.keys():
#     nums = nums + [key]
# nums.sort()
# print(nums)