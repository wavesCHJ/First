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
因为t里的[2,3]可改变，因此t虽然是tuple（不变对象），但是内容实际上是可变的，因此无法hash
"""
