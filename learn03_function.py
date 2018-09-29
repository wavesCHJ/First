
print(abs(-1111))

print(max(1, 2, 6, 4, 3))

#函数名其实就是指向一个函数对象的引用，
#可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-13321))


#把一个整数转换成十六进制表示的字符串
print(hex(255))
print(hex(1023))


def my_abs(x):
    #数据类型检查可以用内置函数isinstance()实现
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x
m = my_abs
print(m(-222))


#如果想定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
#比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
#pass还可以用在其他语句里，比如:
age = 1
if age >= 18:
    pass    
#缺少了pass，代码运行就会有语法错误。


#函数返回多个值
#比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
#但其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi / 6)
print(r)
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
#而多个变量可以同时接收一个tuple，按位置赋给对应的值，
#所以，Python的函数返回多值其实就是返回一个tuple


"""
小结

定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
"""
#practice
"""
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
a*x*x + bx + c = 0
的两个解
"""
def quadratic(a, b, c):
    if a == 0:
        print("a不能为0")
        return
    delt = b * b - 4 * a * c
    if delt < 0:
        return "无解"
    elif delt == 0:
        return -b / (2 * a)
    else:
        return (-b + math.sqrt(delt))/(2*a), (-b - math.sqrt(delt))/(2*a)

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, 4) =', quadratic(1, 3, 4))
print('quadratic(1, 2, 1) =', quadratic(1, 2, 1))


#默认参数
#设置默认参数时，有几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

def enroll(name, gender, age = 6, city = "gaungzhou"):
    print(name, gender, age, city)

enroll("peter", 'M');
enroll("curry", "M", 22, "Golden State")
enroll("waves", "M", 22)
enroll("Mikee", "M", city = "cAL")


def add_end(L = []):
    L.append("end")
    return L
print(add_end())
print(add_end())
print(add_end())
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
#如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end_(L = None):
    if L == None:
        L = []
    L.append("end")
    return L
print(add_end_())
print(add_end_())
print(add_end_(), '\n')




def calc_(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#调用的时候，需要先组装出一个list或tuple：
print(calc_([1,2,3]), calc_((1, 3, 5, 7)));

#可变参数
def calc(*numbers):
    print(numbers)  #传进去后numbers类型变成tuple，内容不可改
    sum = 0
    for n in numbers:
        sum = sum + n * n 
    return sum 
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
#在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
#但是，调用该函数时，可以传入任意个参数，包括0个参数：
print(calc(1,2,3),calc(1,3,5,7), calc())
#如果已有一个list或者tuple，可以在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3, 4, 5]
print(calc(*nums))

#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见


#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('curry', '22')
person('peter', '12', city = 'guangzhou', gender = 'M')

#也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city':'shenzhen', 'height':175}
person('Jimie', '13', **extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
#注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


#命名关键字参数
#如果要限制关键字参数的名字(并强制传入??)，就可以用命名关键字参数，
#例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person2(name, age, *, city, job):
    print(name, age, city, job)
person2('Jack', 22, city = 'shantou', job = 'student')
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person2_(name, age, *args, city, job):
    print(name, age, args, city, job) #此时args后面的city和job参数为命名关键字参数，不是必选参数
person2_('John', 23, 'a', 'b', city = 'shantou', job = 'student')
print('\n')

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c = 0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c = 0, *, d, **kw): #d为命名关键字参数
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x = 99, y = 100)

f2(1, 2, 3, d = 4, z = 101)

def f3(a, b, c = 0, *args, d, **kw): 
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'd =', d, 'kw =', kw)
#a,b为必选参数, c为默认参数, args为可变参数, d为命名关键字参数, kw为关键字参数

f3(1, 2, 3, 'a', 'b', d = 4, x = 100, y = 101)

  

"""
小结
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
"""
#pratice
#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(*args):
    sum = 1
    for num in args:
        sum = sum * num
    print(sum)

product()
product(5, 6)
product(5, 6, 7)
product(5, 6, 7, 9)
print('\n')



#递归函数
def fact(n):
    if (n == 1):
        return 1
    return fact(n - 1) * n
print(fact(5))

#尾递归调用
def fact_iter(num, product):
    if (num == 1):
        return product
    return fact_iter(num - 1, product * num)
print(fact_iter(5, 1))


"""
小结
使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
"""
#practice
#请编写move(n, a, b, c)函数，它接收参数n，
#表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
def move_(n, a, b, c):
    if (n == 1):
        print(a, '-->', c)
    else:
        move_(n - 1, a, c, b)
        move_(1, a, b, c)
        move_(n - 1, b, a, c)
move_(4, 'A', 'B', 'C')


