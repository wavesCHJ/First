#类和实例

#class后面紧接着是类名，即Student，类名通常是大写开头的单词，
#紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
#通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Student(object):
    pass

Snow = Student()
print(Snow) 
print(Student) 
#可以看到，变量Snow指向的就是一个Student的实例，后面的一串值是内存地址，
#每个object的地址都不一样，而Student本身则是一个类。

#可以自由地给一个实例变量绑定属性，比如，给实例Snow绑定一个name属性：
Snow.name = 'John Snow'
print(Snow.name)


#由于类可以起到模板的作用，因此，可以在创建实例的时候，
#把一些我们认为必须绑定的属性强制填写进去。
#通过定义一个特殊的__init__方法，在创建实例的时候，
#就把name，score等属性绑上去：
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

#注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
#因此，在__init__方法内部，就可以把各种属性绑定到self，
#因为self就指向创建的实例本身。

#有了__init__方法，在创建实例的时候，就不能传入空的参数了，
#必须传入与__init__方法匹配的参数，但self不需要传，
#Python解释器自己会把实例变量传进去：
Alan = Student('Alan Walker', 100)
print(Alan.name, Alan.score)

#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
#并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，
#所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

#数据封装
#直接在类中定义函数，对数据进行操作
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
Curry = Student('Stephen Curry', 100)
Curry.print_score()


#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，
#对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
Alan.gender = 'man'
Curry.height = '1.91m'
print(Alan.gender, Curry.height)
print('\n')




#访问限制

#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
#在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
#只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

#改完后，对于外部代码来说，没什么变动，
#但是已经无法从外部访问实例变量.__name和实例变量.__score了
Curry = Student('Stephen Curry', 100)

"""
需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，
并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，
所以，不能用__name__、__score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，
“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
"""
#双下划线开头的实例变量是不是一定不能从外部访问呢？
#其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
#所以，仍然可以通过_Student__name来访问__name变量：
print(Curry._Student__name, ':', Curry._Student__score)


#但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。

#总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

#最后注意下面的这种错误写法：
print(Curry.get_name())
Curry.__name = 'None'
print(Curry.__name)
print(Curry.get_name())
#表面上看，外部代码“成功”地设置了__name变量，
#但实际上这个__name变量和class内部的__name变量不是一个变量！
#内部的__name变量已经被Python解释器自动改成了_Student__name，
#而外部代码给bart新增了一个__name变量。
print('\n')




#继承和多态
class Animal(object):
    def identify(self):
        print('I am an animal')
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

ani = Animal()
dog = Dog()

ani.run()
dog.identify()
dog.run()


a = list()
b = Animal()
c = Dog()
print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))
print(isinstance(b, Dog))

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def Animal_run(animal):
    animal.run()

Animal_run(Animal())
Animal_run(Dog())
Animal_run(Cat())
"""
多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，
就会自动调用实际类型的run()方法，这就是多态的意思：

对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，
就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，
由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，
而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。

这就是著名的“开闭”原则：
对扩展开放：允许新增Animal子类；
对修改封闭：不需要修改依赖Animal类型的Animal_run()等函数。
"""


"""
静态语言 vs 动态语言
对于静态语言（例如Java）来说，如果需要传入Animal类型，
则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。
我们只需要保证传入的对象有一个run()方法就可以了：
"""
class Timer(object):
    def run(self):
        print('Time is running...')

Animal_run(Timer())

"""
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

Python的“file-like object“就是一种鸭子类型。
对真正的文件对象，它有一个read()方法，返回其内容。
但是，许多对象，只要有read()方法，都被视为“file-like object“。
许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，
完全可以传入任何实现了read()方法的对象。
"""
print('\n')






#获取对象信息

#当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
#使用type()
print(type(123))
print(type('skr'))
print(type(None))
print(type(abs))


#type()函数返回对应的Class类型。
#如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print(type(234) == int)
print(type('ss') == str, '\n')

#判断基本数据类型可以直接写int，str等，
#但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x : x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType, '\n')

#使用isinstance()
#对于class的继承关系来说，使用type()就很不方便。
#我们要判断class的类型，可以使用isinstance()函数。
#比如，假设继承关系 object -> Animal -> Dog -> Husky
#那么：
#a = Animal
#d = Dog()
#h = Husky()
#isinstance(h, Animal)  True
#isinstance(d, Husky)   False

#能用type()判断的基本类型也可以用isinstance()判断：
print(isinstance('a', str))
print(isinstance(b'a', bytes))

#并且还可以判断一个变量是否是某些类型中的一种，
#比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1,2,3], (list, tuple)))
print(isinstance((1,2,3), (list, tuple)))    
print()

#使用dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，
#它返回一个包含字符串的list，
#比如，获得一个str对象的所有属性和方法：
print(dir('abc'))

#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
#在Python中，如果你调用len()函数试图获取一个对象的长度，
#实际上，在len()函数内部，它自动去调用该对象的__len__()方法
#剩下的都是普通属性或方法，比如lower()返回小写的字符串

#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyDog(object):
    def __len__(self):
        return 100
print(len(MyDog()))


#仅仅把属性和方法列出来是不够的，
#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'))    #判断是否有x这个属性
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)       #设置y这个属性
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))    #或者y这个属性的值

#如果试图获取不存在的属性，会抛出AttributeError的错误
#可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', 404))

#也可以获得对象的方法，用法和上面一样

#通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
#要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。
print('\n')





#实例属性和类属性

#如果Student类本身需要绑定一个属性
#可以直接在class中定义属性，这种属性是类属性，归Student类所有：
class Student(object):
    name = 'Student'    #我的理解是 跟static变量差不多

print(Student.name)
Mike = Student()
print(Mike.name)
Mike.name = 'Mike Jackson'
print(Mike.name)
del Mike.name
print(Mike.name)
#从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
#因为相同名称的实例属性将屏蔽掉类属性，
#但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。


#practice
#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1
        
curry = Student('Curry')
snow = Student('Snow')
peter = Student('Peter')
print(Student.count)





