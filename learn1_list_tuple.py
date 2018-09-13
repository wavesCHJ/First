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
"""
t = (1, [2, 3])
print(t)
d = {5:6}
d[t] = 2
print(d[t])
"""
"""
报错
TypeError: unhashable type: 'list'

因为t里的[2,3]可改变，因此t虽然是tuple（不变对象），但是内容实际上是变了的，因此无法hash
"""


