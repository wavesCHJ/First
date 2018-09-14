#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'waveschj'

#第1行注释可以让这个文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
#第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
#第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；



#https://www.liaoxuefeng.com/
#模块
"""
请注意，每一个包目录下面都会有一个__init__.py的文件，
这个文件是必须存在的，否则，Python就把这个目录当成普通目录，
而不是一个包。__init__.py可以是空文件，也可以有Python代码，
因为__init__.py本身就是一个模块，而它的模块名就是mycompany。
"""



 
import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World!')
    elif len(args) == 2:
        print('Hello %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()
    
"""
在命令行下运行：

$ python3 hello.py
Hello, world!
$ python hello.py Michael
Hello, Michael!

"""

#作用域
"""
在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。

正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：
"""
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

"""
我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：

外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。

"""

#模块搜索路径
#当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：

#默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

import sys
print(sys.path)


"""
如果我们要添加自己的搜索目录，有两种方法：

一是直接修改sys.path，添加要搜索的目录：

>>> import sys
>>> sys.path.append('/Users/michael/my_py_scripts')
这种方法是在运行时修改，运行结束后失效。

第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。


"""









