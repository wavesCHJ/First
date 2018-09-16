
class Student(object):
    pass

s1 = Student()
#给实例动态绑定属性
s1.name = 'Curry'
#给实例动态绑定方法
def set_age(self, age):
    self.age = age

from types import MethodType
s1.set_age = MethodType(set_age, s1) # 给实例绑定一个方法
s1.set_age(25)

print(s1.name, ':', s1.age)  # 测试结果

#给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
#s2.set_age(100)  #报错

#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score
Student.set_score = set_score
#给class绑定方法后，所有实例均可调用：
s1.set_score(100)
s2.set_score(101)
print(s1.score, s2.score)

#通常情况下，上面的set_score方法可以直接定义在class中，
#但动态绑定允许我们在程序运行的过程中动态给class加上功能，
#这在静态语言中很难实现。



#使用__slots__

#但是，如果我们想要限制实例的属性怎么办？
#比如，只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，
#定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Snow'
s.age = 23
#s.score = 100
#由于'score'没有被放到__slots__中，所以不能绑定score属性，
#试图绑定score将得到AttributeError的错误。


#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，
#对继承的子类是不起作用的：
class SeniorStudent(Student):
    pass
s = SeniorStudent()
s.score = 999
print('\n')




#使用@property

#有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
#Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student(object):
    @property
    def score(self):  #把score属性当成方法写，然后在方法前加@property
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must be between 0~100!')
        self._score = value

    @property
    def age(self): #只读属性，没有创建setter()装饰器
        return 25

#把一个getter方法变成属性，只需要加上@property就可以了，
#此时，@property本身又创建了另一个装饰器@score.setter，
#负责把一个setter方法变成属性赋值，
#于是，我们就拥有一个可控的属性操作：
s = Student()
s.score = 60
#s.score = 150
print(s.score, s.age)
     
#practice
#请利用@property给一个Screen对象加上width和height属性，
#以及一个只读属性resolution：
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if value > 0 and value < 100000:
            self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if value > 0 and value < 100000:
            self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.height = 1024
s.width = 768
print(s.resolution)
    





#多重继承
class Animal(object):
    pass

class Runnable(object):
    pass

class Dog(Animal, Runnable):
    pass
print('\n')




#定制类

#__str__ (相当于java的toString()函数)
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
    
print(Student('Curry'))


#__iter__
#如果一个类想被用于for ... in循环，类似list或tuple那样，
#就必须实现一个__iter__()方法，该方法返回一个迭代对象，
#然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
#直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self         # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a    # 返回下一个值

for n in Fib():
    print(n, end = ' ')
print()



#__getitem__
#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):   #n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): #n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

            
f = Fib()
print(f[5], f[100])
print(f[0:10])


#__call__  (把对象本身当函数用)
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self, *args, **kw):
        print('My name is %s' % self.name)
s = Student('Jerry')
s()
s(1)
















