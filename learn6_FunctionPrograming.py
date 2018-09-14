#返回函数

#函数作为返回值
#求和函数，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
#可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
#调用函数f时，才真正计算求和的结果：
print(f())

#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)
 
def lazy_sum2(L):
    def sum():
        ax = 0
        for n in L:
            ax = ax + n
        return ax
    return sum
l = [1, 2, 3, 4]
f = lazy_sum2(l)
print(f())
l.append(5)
print(f())

#闭包
#注意到返回的函数在其定义内部引用了局部变量args，
#所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用

#另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。
#我们来看一个例子：
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
#在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
f1, f2, f3 = count()
print(f1(), f2(), f3())
#你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
#等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

###返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

#如果一定要引用循环变量怎么办？
#方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
#无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count2():
    fs = []
    def f(j):
        def g():
            return j * j
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count2()
print(f1(), f2(), f3())

#pratice
#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    n = [0]
    def counter():
        n[0] = n[0] + 1
        return n[0]
    return counter
f = createCounter()
print(f(), f(), f(), f())

def createCounter2():
    global n
    n = 0
    def counter():
        global n
        n = n + 1
        return n
    return counter
f = createCounter2()
print(f(), f(), f(), f())








#匿名函数 
#当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
l = list(map(lambda x: x * x, [1, 2, 3, 4]))
print(l)

#关键字lambda表示匿名函数，冒号前面的x表示函数参数。

#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。

#此外，匿名函数也是一个函数对象，
#也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x : x * x
print(f(6))

#同样，也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y
f = build(3, 4)
print(f())

#practice
#找奇数
l = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(l)










#装饰器
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def print_now():
    print('2018.9.14 11:15')
f = print_now
f()
#函数对象有一个__name__属性，可以拿到函数的名字：
print(f.__name__, print_now.__name__, '\n')

#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
#但又不希望修改now()函数的定义，
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

#本质上，decorator就是一个返回函数的高阶函数。
#所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw) #这里是调用传进来的函数（原始函数）
    return wrapper

@log
def now():
    print('2018.9.14 11:22')
    return 'Finish'
print(now())
#把@log放到now()函数的定义处，相当于执行了语句：
#now = log(now)

#但是，__name__已经从原来的'now'变成了'wrapper'：
print('__name__已经从原来的now变成了: ', now.__name__, '\n')

#因为返回的那个wrapper()函数名字就是'wrapper'，
#所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
#否则，有些依赖函数签名的代码执行就会出错。

#不需要编写wrapper.__name__ = func.__name__这样的代码，
#Python内置的functools.wraps就是干这个事的，
#所以，
#一个完整的decorator的写法如下：
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2018.9.14 13:49')
    return 'Finish'
print(now())
print('现在的__name__: ', now.__name__, '\n')


#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
#写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def decorator(func):     #如果传入参数，就再建一层函数
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2018.9.14 11:39')
    return 'End'
print(now())
print('__name__ : ', now.__name__, '\n')

#相当于执行
#now = log('execute')(now) 
#print(now(), '\n')


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('ececute')
def now():
    print('2018.9.14 14:09')
    return 'End'
print(now())
print('__name__ : ', now.__name__, '\n')




#practice
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def decorator(*args, **kw):
        start = time.time()
        result = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return result
    return decorator

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y
@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
print()

"""
写出一个@log的decorator，使它既支持：
@log
def f():
    pass

又支持：
@log('execute')
def f():
    pass
"""
from inspect import isfunction
def log(arg = ''):
    if type(arg) == str:  #如果传入参数，就再建一层函数
        def decorator(fn):
            def wrapper(*args, **kw):
                print('execute %s %s' % (arg, fn.__name__))
                return fn(*args, **kw)
            return wrapper
        return decorator
    if isfunction(arg):
        def decorator(*args, **kw):
            print('call %s' % arg.__name__)
            return arg(*args, **kw)
        return decorator
@log('func')
def f(x, y):
    print('x + y  = ', x + y)

@log
def g(x, y):
    print('x * y = ', x * y)

f(1, 2)
g(1, 2) 














