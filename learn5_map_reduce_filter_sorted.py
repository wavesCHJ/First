#map/reduce

#我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x

r = map(f, [1,2,3,4,5])
print(list(r))
r = map(str, [1,2,3,4,5])
print(list(r))


#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
#其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))  #相加的和

def add2(x, y):
    return x * 10 + y
print(reduce(add2, [1, 3, 5, 7, 9]))  #将序列变为一个数

#把str转换为int的函数
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(c):
        return ord(c) - 48
    return reduce(fn, map(char2num, s))
print(str2int('12344') + 1)


#practice

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def fun1(s):  
    return s[:1].upper() + s[1:].lower()
print(list(map(fun1, ['adam', 'LISA', 'barT'])))
#字符串是不可变对象，因此不能直接改变字符串的内容，一般是重新生成一个
#字符串修改某一个位置的字符,
#一种可行的方式，是将字符串转换为列表，修改列表的元素后，再重新连接为字符串
s = 'abcdefghijk'
l = list(s)
l[0] = 'A'
newS = ''.join(l)
print(newS)


#请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def fun_p(x, y):
        return x * y
    return reduce(fun_p, L)
print(prod([1,2,3,4,5]))
print('\n')





#filter
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5])))

#把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
l = list(filter(not_empty,  ['A', '', 'B', None, 'C', '  ']))
print(l)


#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    return (str(n) == str(n)[::-1]) #string[::-1] 字符串翻转
l = list(filter(is_palindrome, [12321, 12345, 34543, 909]))
print(l)
print('\n')






#sorted
#排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，
#但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，
#因此，比较的过程必须通过函数抽象出来

#Python内置的sorted()函数就可以对list进行排序：
l = sorted([36, 5, -12, 9, -21])
print(l)


#此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，
#例如按绝对值大小排序：
l = sorted([36, 5, -12, 9, -21], key = abs)
print(l)

l = sorted(['bob', 'about', 'Zoo', 'Credit'])
#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
print(l)

l = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True)
#忽略大小写的排序，并且反向排序
print(l)

#practice

#假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序
def sort_by_name(t):
    return t[0]
#再按成绩从高到低排序：
def sort_by_grade(t):
    return t[1]

l = sorted(L, key = sort_by_name)
print(l)
l = sorted(L, key = sort_by_grade, reverse = True)
print(l)











