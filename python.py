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
    >> def gen_ab():
           print('start...')
           yield 'a'
           print('continue....')
           yield 'b'
           print('end')
    ...
    >> for c in gen_ab():
           print('-->',c)
    ...
    start...
    -->a
    continue....
    -->b
    end
'''
