""" 输入
name = input("please iuput your name:")
print(name+"\n)
"""

#Python还允许用r''表示''内部的字符串默认不转义
print(r"i'am \"OK\"\n, and you\n") 
#各种类型的输出，直接逗号分开就行了
print("Hello", 111, " World!", True, '\n')


#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
#当然，这应该是在命令行下敲才会用到的吧
print('''first line
second line
third line''')

if True:
	print("True")
if not False:
	print("not False")
if True or False:
	print("True or False\n")

#空值为None

"""
1.在内存中创建了一个'ABC'的字符串；
2.在内存中创建了一个名为a的变量，并把它指向'ABC'。
3.在内存中创建了一个名为b的变量, 并把变量b指向变量a所指向的数据
4.在内存中创建了一个'XYZ'的字符串, 并把变量a指向"XYZ"
"""
a = 'ABC'
b = a
a = 'XYZ'
print('a = ' + a + ' b = ' + b + '\n')


#有一种除法是//,称为地板除,只取结果的整数部分
print(10 / 3)
print(9 / 3)
print(10 // 3)
print('\n')

#Python的整数没有大小限制,Python的浮点数也没有大小限制.
#但是超出一定范围就直接表示为inf（无限大）

#Python的字符串

#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示
# chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\n')


#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
#如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#Python对bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'
print(x)
#bytes的每个字符都只占用一个字节,而Unicode一般是2个字节
print(len(x))
print('\n')

#输出格式化
print("输出中文！")
print("Hello, %s" % "world")
print('Hi, %s, you have $%d.' % ('waves', 1000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
#如果不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串

#pratice
s1 = 72
s2 = 85
r = (85 - 72) / 72 * 100
print('小明成绩提升的百分比为:%.1f%%'% r)


#另一种格式化字符串的方法是使用字符串的format()方法，
#它会用传入的参数依次替换字符串内的占位符{0}、{1}……
print('Hello, {0}, 成绩提升了{1:.1f}%'.format('小明', 17.125))
print('\n')



#条件判断
age = 9
if age >= 18: 
        print("adult")
elif age >= 6: 
        print("teenager")
else: 
        print("kid")

#只要X是非零数值、非空字符串、非空list等，就判断为True，否则为False
X = [0]
if X:
        print("True")

"""
s = input("birth:")
#输入后,获取的值类型为字符串类型,所以要转为整数类型才能比较
birth = int(s)
if birth < 2000:
        print("00前")
else:
        print("00后")
"""

#pratice
"""
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）
帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
"""
height = 1.75
weight = 80.5
bmi = weight / height / height
if bmi < 18.5:
        print("过轻")
elif bmi >= 18.5 and bmi < 25:
        print("正常")
elif bmi >= 25 and bmi < 28:
        print("过重")
elif bmi >= 28 and bmi < 32:
        print("肥胖")
else:
        print("严重肥胖")
print('\n\n')




#循环
names = ["make", 'curry', 'waves']
for name in names:
        print(name)
#Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
x = 5
print(range(x))
print(list(range(x)))

#计算0-100的和
sum = 0
for x in range(101): #for循环
        sum = sum + x
print("sum = ", sum)
sum = 0
n = 100
while n > 0:     #while循环
        sum = sum + n
        n = n - 1
print("sum = ", sum)

#---------------------------------------------#---------------------------------------------#---------------------------------------------#---------------------------------------------#---------------------------------------------#---------------------------------------------#---------------------------------------------
#---------------------------------------------
#---------------------------------------------#---------------------------------------------

listArr = ['aaa', 'bbb', 'ccc']
print(listArr)
print(len(listArr))

#用-1做索引,直接获取最后一个元素
#-2获取倒数第二个,-3倒数第三个,以此类推
print(listArr[-1])
print(listArr[-2])

#添加元素到末尾
listArr.append('ddd')
#插入元素到指定位置
listArr.insert(2, 'eee')
print(listArr)
#删除list末尾的元素,返回删除的元素
print(listArr.pop())
#删除指定位置的元素,返回删除的元素
print(listArr.pop(0))
#把某个元素替换成其他元素
listArr[0] = 'fff'

#list里面的元素的数据类型也可以不同
lists = ['A', 1, True]

#list元素也可以是另一个list
#这时的list可以认为是多维数组
lists = ['a', 'b', ['aa', 0, 'bb'], 'c']
print("{0}  len = {1}".format(lists, len(lists)))
print('lists[2][2] = %s' % lists[2][2])
print('\n')


#另一种有序列表叫元组：tuple
#tuple和list非常类似,但是tuple一旦初始化就不能修改
tupleArr = ('aa', 'bb', 'cc')
print(tupleArr)

"""
tuple没有append()，insert()这样的方法。
其他获取元素的方法和list是一样的，可以正常地使用tupleArr[0]，tupleArrs[-1]，但不能赋值成另外的元素。

不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
"""


#要定义一个只有1个元素的tuple，如果你这么定义：
t = (1)
print(t)
"""
定义的不是tuple，是1这个数！
这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，
因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。

所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
"""
t = (1, )
print(t)

#最后来看一个“可变的”tuple：
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
"""
tuple一开始指向的list并没有改成别的list,
所以,tuple所谓的“不变”是说,tuple的每个元素，指向永远不变.
即指向'a',就不能改成指向'b',
指向一个list,就不能改成指向其他对象,但指向的这个list本身是可变的.
"""






#---------------------------------------------#---------------------------------------------
#---------------------------------------------
#---------------------------------------------#---------------------------------------------#---------------------------------------------
#---------------------------------------------



        




		
		






dic = {'tom':90, 'curry':233, 'waves':23333}
print(dic['curry'])

dic['john'] = 20000;
print(dic['john'])

#如果key不存在，dict就会报错
#要避免key不存在的错误，有两种办法，
#一是通过in判断key是否存在
print('jack' in dic)
#二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(dic.get('jack'))
print(dic.get('jack', -1))

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
dic.pop('tom')
print(dic)
#正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象
#在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key
#而list是可变的，就不能作为key


#set和dict类似，也是一组key的集合，但不存储value

#要创建一个set，需要提供一个list作为输入集合：
s = set([1, 3, 2, 3, 1])
print(s)
s.add(5)
s.add(4)
s.add(2)
print(s)
s.remove(3)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2])
s2 = set([2, 3])
print(s1 | s2)
print(s1 & s2)





#再议不可变对象
#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
a = ['c', 'b', 'a']
a.sort()
print(a)

#而对于不可变对象，比如str，对str进行操作，内容不变
a = 'abc'
print(a.replace('a', 'A'))
print(a)
#相当于
a = 'abc'
b = a.replace('a', 'A')
print(a, b)

#tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中
"""
t = (1, [2, 3])
print(t)
d = {5:6}
d[t] = 2
print(d[t])
"""
