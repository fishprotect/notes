#python注意事项
1 注意导入包和当前文件夹重名
eg:$ import requests时，如果该文件的名字是：requests.py,则就会出错。
    会出现，导入的文件中没有你要的方法或者对象
    
# 装饰器

### 方法一：
@decorate
def target():
    print('running target()')

### 方法二：
def target():
    print('running target()')
decorate(target)

'''
    如上，装饰器只是语法糖
    特性1：能把被装饰的函数换成其他函数
    特性2：装饰器在加载模块时，立即执行（在被装饰的函数执行后立即执行）
'''
### 有以下文件，resgistration.py
registry = []
def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func
@register
def f1():
    print("running f1()")
@register
def f2():
    print("running f2()")
def f3():
    print("running f3()")
def main():
    print("running main()")
    print('registry ->',registry)
    f1()
    f2()
    f3()
### 猜想运行该文件的结果（答案：流畅的python，Page：157）

# 闭包
'''
    1 闭包是指 延伸了作用域的函数
    2 只有涉及嵌套时，才会有闭包的概念
    3 能访问定义体之外的非全局变量（自由变量）
'''
### 闭包的实现如下
def make_average():
    series = []                     # 自由变量（定义的自由体以外的非全局变量）
    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

# 生成器和迭代器
## 区分 迭代器和可迭代的对象
'''
    迭代器的两个方法：
    1 __iter__ :返回self 以便在使用该迭代器对象的地方使用迭代器
    2 __next__ :返回下一个可用元素
'''

## 生成器，生成器是迭代器
'''
    1 调用生成器函数返回生成器，生成器生成或者产出值
    如下实例：展示生成器的运行过程
    >>> def gen_ab():
           print('start...')
           yield 'a'
           print('continue....')
           yield 'b'
           print('end')
    ...
    >>> for c in gen_ab():
           print('-->',c)
    ...
    start...
    -->a
    continue....
    -->b
    end

    2 列表推导和生成器表达式的比较
      1)列表推导
    >>> res1 = [x*3 for x in gen_ab()]  # res1 = ['--->aaa','--->bbb']
    satrt...
    continue....
    end.
    >>> for i in res1:
            print(i)
    ...
    --->aaa
    --->bbb
      2）生成器表达式
    >>> res2 = (x*3 for x in gen_ab()) # res2 =
    >>> for i in res2:
            print(i)
    ...
    start...
    --->aaa
    continue....
    --->bbb
    end 
'''
# 制作生成器时，优先选用生成器函数
# 方法一：实现生成器
# 如下，为了构生成器而构建__iter__方法
class A:
    def __init__(self,begin,step,end):
        self.begin = begin
        self.step = step
        self.end = end
    def __iter__(self):
        result = type(self.begin+self.end)(self.begin)
        forever = self.end is None
        while forever or result < self.end:
            yield result
            result = result+self.step
# 方法二：实现生成器
# 如下是：使用生成器函数 制造生成器
# 生成器函数：在python函数的定义体中，有yield关键字，该函数就是生成器函数
def B(begin,step,end=None):
    result = type(begin+step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + index*step

'''
    #深入分析iter函数
    >>> def d6():
          return rnadint(1,6)
    ...
    >>> d6_iter = iter(d6,1)    # 第二个参数 1 为哨符，是标记值，可调用的对象返回这个值时、
                                # 触发迭代器，抛出StopIteration异常，而不产出哨符
    # 如下函数，逐行处理文件，直到遇到空行或者到达文件末尾
    with open('mydata.txt') as fp:
        for line in iter(fp.readline,'\n'):
            process_line(line) # process_line()函数是处理行的函数
'''
