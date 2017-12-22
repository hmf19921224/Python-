# coding=utf-8

import math
'''
适用于首选是网络应用，包括网站、后台服务等等；
其次是许多日常需要的小工具，包括系统管理员需要的脚本任务等等；
整数：1；100；1000；

布尔值可以用and、or和not运算。
与ios相似 and 并运算 or 或运算 not 非运算


浮点数 1.3 ； 3.14； -9.2
bool值 表示 False或者 True 区分大小写。
字符串 以双引号或者单引号圈起的字符串 “abc”或 ‘abc’
变量分为静态或者动态变量


'''

print("hello world")
print("我的世界")

# 转义如果字符串内同时包含'和"那么需要用转义字符去标识
print("i\'\\m ok\"")
print("ad'b")
print("ad'\"b")
print('\\ab\\v')
# 动态变量。可以赋值给不同的类型
t_007 = 'T007'

t_007 = 20
# 静态变量 固定了类型。不可以转变

t_008 = "2000"

# error int t_008 = 20


print(t_008)

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

ord('c')
chr(55)

ord('d')

print(ord('文'))

print(ord('\u4e2d'))

x = b'ABC'
print('x is %s' % x)

# len()计算的是字符串包含的字符数量。而字符串转变成byte后。len计算的是字符串所占用的字节数量
x = len('中文'.encode('utf-8'))
print(x)
x = len('中文')
print(x)
'''
插入字符串。%s表示字符串。%d是数字
你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，
%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
'''

'Hi, %s, you have $%d.' % ('Michael', 1000000)

'%2d-%02d' % (3, 1)

print ('Hi,%.1f' % 9.99)

s1 = 72
s3 = 85

print('小明的成绩是%.1f' % ((s3 - s1) / s1 * 100))

# list 就是ios中的数组

mathArray = ["中文", '数组', '小学']
len(mathArray)
# 也是从0开始。但是有一个索引值-1.取到最后一个元素的值。以此类推，可以获取倒数第2个、倒数第3个：

# list是一个可变的有序表，所以，可以往list中追加元素到末尾：

mathArray.append(3)

# 插入元素的位置

mathArray.insert(1, '5')

# 删除  要删除list末尾的元素，用pop()方法：要删除指定位置的元素，用pop(i)方法，其中i是索引位置：

mathArray.pop()
mathArray.pop(2)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：

mathArray[2] = "24"

classmates = ('Michael', 'Bob', 'Tracy')
# tuple元祖 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。可以取值。但是不同赋值与添加


# 条件判断

age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

else:

    print('error')

# birth = input('birth:')
#
# if int(birth) > 1992:
#     print('超过了年线%s' % (birth))

# 循环

names = ['Michael', 'Bob', 'Tracy']

for name in names:
    print(name)

    # 0到100
    sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# 当循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 字典dictionary

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']

d['Adam'] = 67
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：

'Thomas' in d

d.get('Thomas')

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')

# set 不重复的key的集合
s = set([1, 1, 2, 2, 3, 3])

print('16进制的%s' % (hex(254)))


# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:

def 绝对值(x):
    if x > 20:
        return x
        # pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

defs = 绝对值

defs(5)
def 数值(d):
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(10, 20, 30, math.pi / 6)


def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('bad operand type')


def test(x=None):
    x = []
    x.append('END')

    test()

def pip(conet ,host ):

    x = 5
    print('x = %d' %x)
    return  x


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('json', 18)

person('bob', 35, jab='jar')


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：

def person1(name, age, *, city, job):
    print(name, age, city, job)


person1('card', 18, city='xini', job='java')
person1('card', 18, city='xini', job='java')

power(4)


def person(name, age, *args, city, job):
    print('iab', 18, (18, 'gb'), city='xoni', job='java')


def person2(a, b, *args, **kw):
    print(a, b, args, kw)


person2(3, 4)

person2(4, 36, 4, "adb", kw="c")


def digui(x):
    if x > 1:
        return 1
    else:
        return x * digui(x - 1)

    digui(5)


from collections import Iterable

isinstance('abc', Iterable)

l = list(range(1, 11))
print(l)

s = [x * x for x in range(1, 11)]

s2 = [x * x for x in range(1, 11) if x % 2 == 0]

g = (x * x for x in range(1, 11))

g1 = (5, 'c', 'b')
next(g)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


o = odd()
next(o)
next(o)
next(o)


# 迭代器 yield是迭代器的标志
def fib(max):
    print('这是一个n')

    n, a, b = 0, 0, 1
    print('这是一个n1')

    while n < max:
        print('这是一个%d' % n)
        yield b
        print('这是一个%d' % n)
        a, b = b, a + b
        n = n + 1
    return 'done'


o = fib(3)
print(next(o))
print(next(o))

print(next(o))


def gener(raw):
    n, a = 1, [1]
    while n <= raw:
        yield (a)
        b = a[:]
        for i in range(n - 1):
            a[i + 1] = b[i] + b[i + 1]
        n += 1
        a.append(1)


for num in gener(10):
    print(num)


    # map映射函数


def maps(x):
    return x * x


map(maps, [1, 4, 8])

# 个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，

from functools import reduce


def add(x, y):
    return x + y


reduce(add, [1, 3, 5, 7, 9])

# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list：


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def sortss(*t):

    return t[0]


l2 =sorted(L, key=sortss)

for tumple in l2:

    print(tumple)
#函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

le = lazy_sum((1,3,5,6))

#函数对象有一个__name__属性，可以拿到函数的名字：

lazy_sum().__name__

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

log(lazy_sum)(45)




#装饰器


def logs(func):

    def wrapper(*args,**kw):
        print('call begain')
        func(*args,**kw)
        print('call end')
    return  wrapper

@logs
def now():
       print('2015-3-25')
now()

#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：

int('12345', base=8)

class student(object):

    def __init__(self,name, idd):
        self.name = name
        #在变量之前加_外部访问不到
        # 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
        self.__id = idd

    def get__id( self ):

         return self.__id


let = student('jack',200)

let.name



#python的类属性和实例属性不一致。

class test(object):


    id = 'kae'
    def __init__(self,name):
        self.name = name


tes = test('kake')
tes.id


def set_age(self,age):
    self.name = age

#python动态语言。可以给类绑定一个方法
from types import MethodType
tes.set_age = MethodType(set_age, 's') # 给实例绑定一个方法


class Students(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


