#文件读写

try:
    f = open('in.txt', 'r')
    #调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
    print(f.read())
#关闭文件
finally:
    if f:
        f.close() 

#更简洁的写法
with open('in.txt', 'r') as f:
    print(f.read())
#这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。

#调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
#所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
#另外，调用readline()可以每次读取一行内容，
#调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

#如果文件很小，read()一次性读取最方便；
#如果不能确定文件大小，反复调用read(size)比较保险；
#如果是配置文件，调用readlines()最方便：
with open('in.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip()) #把末尾的'\n'去掉


#file-like Object

#像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
#除了file外，还可以是内存的字节流，网络流，自定义流等等。
#file-like Object不要求从特定类继承，只要写个read()方法就行。

#StringIO就是在内存中创建的file-like Object，常用作临时缓冲。


#二进制文件
#前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。
#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
with open('test.jpg', 'rb') as f:
    print(f.read(100))


#字符编码
#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，
#例如，读取GBK编码的文件：
with open('in.txt', 'r', encoding='gbk') as f:
    print(f.read())


#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
#因为在文本文件中可能夹杂了一些非法编码的字符。
#遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。
#最简单的方式是直接忽略：
with open('in.txt', 'r', encoding = 'gbk', errors = 'ignore') as f:
    print(f.read())


#写文件
#写文件和读文件是一样的，唯一区别是调用open()函数时，
#传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
with open('in.txt', 'r', encoding = 'gbk') as fin:
    with open('out.txt', 'w', encoding = 'gbk') as fout:
        fout.write(fin.read())

#讲'w'改成'a'以追加（append）模式写入
print('\n')





#StringIO

#很多时候，数据读写不一定是文件，也可以在内存中读写。
#StringIO顾名思义就是在内存中读写str。
#要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
from io import StringIO
f = StringIO()
print(f.write('hello'))  #f.write()返回写入的长度
print(f.write(' '))
f.write('world!')
print(f.getvalue()) # getvalue()方法用于获得写入后的str

#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f = StringIO('Hello!\nHow are you?\n') 
while True:
    s = f.readline() #这里是初始化就传入了字符串，因此指针位置没变，还在开头（0）那里
    if s == '':
        break
    print(s.strip())



# 如果你用file-like object的方法查看的时候，你会发现数据为空
sio = StringIO()
sio.write('test sentence\nggg\nhhh\n')
while True:
    s = sio.readline() 
    if s == '':
        break
    print(s.strip())#输出为空，因为write()函数调用后，文件指针位置在末尾

# 这时候我们需要修改下文件的指针位置
print('pos:', sio.tell())   
sio.seek(0, 0)              
    # tell 方法获取当前文件读取指针的位置
    # seek 方法，用于移动文件读写指针到指定位置,有两个参数，
    #   第一个offset: 偏移量，需要向前或向后的字节数，正为向后，负为向前；
    #   第二个whence: 可选值，默认为0，表示文件开头，1表示相对于当前的位置，2表示文件末尾
print('pos:', sio.tell())
while True:
    s = sio.readline() 
    if s == '':
        break
    print(s.strip())

print('\n')




#BytesIO
    
#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
#BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())
#请注意，写入的不是str，而是经过UTF-8编码的bytes。

#和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
b = f.read()
print(b)
s = bytes.decode(b) #bytes to str
print(s)
print(str.encode(s)) #str to bytes
print('\n')

 
#小结
#StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。





#操作文件和目录

import os
print(os.name) # 操作系统类型
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

#环境变量
#在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
#print(os.environ)   #太多了就不打印了
#要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('PATH'), '\n')

#查看当前目录的绝对路径
path = os.path.abspath('.')
print(path)
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
new_dir = os.path.join(path, 'test_dir')
print(new_dir)
# 然后创建一个目录:
os.mkdir(new_dir)
# 删掉一个目录:
os.rmdir(new_dir)

#把两个路径合成一个时，要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。

#要拆分路径时，要通过os.path.split()函数，
#这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split(new_dir))

#os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
txt_path = os.path.join(path, 'in.txt')
if os.path.isfile(txt_path):  #判断文件是否存在
    print(os.path.splitext(txt_path))

new_dir = os.path.join(path, 'testdir')
if os.path.exists(new_dir) == False:   #判断文件夹是否存在
    os.mkdir(new_dir)

with open('a.txt', 'w') as f:  #创建a.txt
    pass
#文件重命名 
os.rename('a.txt', 'b.txt')
#删除文件
os.remove('b.txt')

#shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

#列出当前目录下的所有.py文件，只需一行代码：
l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(l)
print('\n')

#利用os模块编写一个能实现dir -l输出的程序。
with os.scandir('.') as it:
    for entry in it:
        print(entry.name.encode('utf-8'))

#practice
        
#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
#并打印出相对路径。
def my_find2(s):
    path=s
    #key=input('请输入要查询的文件名关键字:\n')
    key = 'in.txt'
    for root,dirs,files in os.walk(path):
        for name in files:
            if key in name:
                print(name)
                print('相对路径：%s\n'%os.path.relpath(os.path.join(root,name),path))
#path=input('请输入要查询的目录路径：\n')

#在当前文件夹下找文件in,txt                
path = os.path.abspath('.')  
my_find2(path)

print('\n')






#序列化
import pickle
d = dict(name = 'Bob', age = 20, score = 88)
print(pickle.dumps(d))
#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。

#或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)
#看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。


#当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
#然后用pickle.loads()方法反序列化出对象，
#也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
#我们打开另一个Python命令行来反序列化刚才保存的对象：


with open('dump.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)

#Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
#并且可能不同版本的Python彼此都不兼容，
#因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
print('\n')





#JSON
#JSON和Python内置的数据类型对应如下：
"""
JSON类型	Python类型
{}	          dict
[]	          list
"string"	  str
1234.56	          int或float
true/false	  True/False
null	          None
"""s
#Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json
d = dict(name = 'Bob', age = 20, score = 88)
print(json.dumps(d))

#.....略....

















