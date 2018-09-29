#切片
#取一个list或tuple的部分元素是非常常见的操作
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取前3个元素
print(L[0:3])
#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
#如果第一个索引是0，还可以省略
print(L[:3])
print(L[-2:-1])
print(L[-3:])
#倒数第一个元素的索引是-1
L = list(range(100))
#所有数，每10个取一个：
print(L[::10])
#前20个数，每2个取一个
print(L[:20:2])
#最后20个数，每4个取一个
print(L[-20::4])

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
s = 'ABCDEFGHIJK'
print(s[:4])
print(s[::2])

#practice
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    while (len(s) > 0 and s[0] == ' '):
        s = s[1:]
    while (len(s) > 0 and s[-1] == ' '):
        s = s[:-2]
    print(s)
trim('     ')
trim('hello  ')
trim('  hello')
trim('   hello world  ')



#迭代
#只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key, ':', d[key], '', end = '')
print()
#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，
#如果要同时迭代key和value，可以用for k, v in d.items()。
for value in d.values():
    print(value, '', end = '')
print()
for k, v in d.items():
    print(k, ':', v, '', end = '')
print()

#字符串也是可迭代对象，因此，也可以作用于for循环：
for c in 'ABCD':
    print(c, end = ' ')
print()
#判断一个对象是可迭代对象
from collections.abc import Iterable
print(isinstance('abc', Iterable))
print(isinstance(12345, Iterable))

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
L = ['a', 'b', 'c']
for i, value in enumerate(L):
    print(i, ':', value, end = ' ', sep = '')
print()

#print()函数的参数，sep表示字符串之间的连接符，end表示以什么结尾
#默认sep=' '，end='\n'，

#for循环里，同时引用了两个变量
for x, y in [(1,1), (2,4), (3,9)]:
    print(x, y)

#practice
#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if (len(L) == 0):
        return (None, None);
    maxi = L[0]
    mini = L[0]
    for val in L:
        maxi = max(val, maxi)
        mini = min(val, mini)
    return (mini, maxi)

#测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
print('\n')



#列表生成式
L = list(range(10, 20))
print(L)
#生成[1x1, 2x2, 3x3, ..., 10x10]
L = [x * x for x in range(1, 11)]
print(L)
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)
#还可以使用两层循环，可以生成全排列：
L = [m + n for m in 'abc' for n in 'xyz']
print(L)
#三层和三层以上的循环很少用

#列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录

#列表生成式也可以使用两个变量来生成list
d = {'x':'A', 'y':'b', 'z':'c'}
print([k + '=' + v for k, v in d.items()])

#把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

#practice
#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
#使用内建的isinstance函数可以判断一个变量是不是字符串
#请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)







#生成器
#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
#而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
#如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

#如果列表元素可以按照某种算法推算出来，那我们可以在循环的过程中不断推算出后续的元素,
#这样就不必创建完整的list，从而节省大量的空间。
#在Python中，这种一边循环一边计算的机制，称为生成器：generator。

#要创建一个generator，有很多种方法。
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(L)
print(next(g), next(g), next(g))
#generator也是可迭代对象，可以用for循环
for n in g:
    print(n, end = ' ')
print() 

#斐波拉契数列
#函数版本
def fib_1(maxi):
    n, a, b = 0, 0, 1
    while n < maxi:
        print(b, end = ' ')
        a, b = b, a + b
        n = n + 1
    return 'done'
fib_1(6)
print()

#生成器版本
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，
#而是一个generator：
def fib_2(maxi):
    n, a, b = 0, 0, 1
    while n < maxi:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib_2(6))
#generator和函数的执行流程不一样。
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。\
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句停住，然后返回，
#再次执行时从上次返回的yield语句处继续执行。

#举个简单的例子，定义一个generator，依次返回数字1，3，5：
def odd():
    print('step 1: ', end = ' ')
    yield 1
    print('step 2: ', end = ' ')
    yield 3
    print('step 3: ', end = ' ')
    yield 5
#调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
o = odd()
print(next(o))
print(next(o))
print(next(o))

#使用for循环来迭代：
for n in fib_2(6):
    print(n, end = ' ')


#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
#如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib_2(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break;

#practice
"""
杨辉三角定义如下：
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list
"""

def triangles(n):
    c = 0;
    L = [1]
    while c < n:
        yield L
        L2 = [1]
        for i, v in enumerate(L):
            if (i < len(L) - 1):
                L2.append(L[i] + L[i+1])
        L2.append(1)
        L = L2
        c = c + 1
        
g = triangles(5)
while True:
    try:
        L = next(g)
        print(L)
    except StopIteration as e:
        break;

#比较牛批的写法
def triangles_(n):
    c = 0;
    L = [1]
    while c < n:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]
        c = c + 1
        
g = triangles_(5)
while True:
    try:
        L = next(g)
        print(L)
    except StopIteration as e:
        break

print('\n')






#迭代器

#我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#可以使用isinstance()判断一个对象是否是Iterable对象：
from collections.abc import Iterable
print(isinstance([], Iterable))
print(isinstance((x for x in range(10)), Iterable))


#而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#可以使用isinstance()判断一个对象是否是Iterator对象：
from collections.abc import Iterator
print(isinstance([], Iterator))
print(isinstance((x for x in range(10)), Iterator))

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))




