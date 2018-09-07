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














        




