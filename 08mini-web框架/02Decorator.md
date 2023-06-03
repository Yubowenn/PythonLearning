# 装饰器

## 1 介绍
### 1.1 概念
* 给已有函数增加额外功能的函数，它本质上就是一个闭包函数
* 特点：
  * 不修改已有函数的源代码
  * 不修改已有函数的调用方式
  * 给已有函数增加额外的功能
### 1.2 示例
```python
# 添加一个登录验证的功能
def check(fn):
    print("装饰器函数执行了")
    def inner():
        print("请先登录....")
        fn()
    return inner

# 使用语法糖方式来装饰函数
# @check => comment = check(comment)
@check
def comment():
    print("发表评论")

comment()

# 输出：
# 请先登录....
# 发表评论
```
* @check 等价于 comment = check(comment)
* 装饰器的执行时间是加载模块时立即执行。

## 2 装饰器的使用场景
对已有函数进行功能扩展时
* 示例1：统计函数执行的时间
```python
import time

def get_time(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print('函数执行花费：', end_time-start_time)

    return inner
```

## 3 通用装饰器：可以装饰任意的函数
```python
def decorator(func):
    def inner(*args, **kwargs):
        print('程序正在执行...')
        num = func(*args, **kwargs)
        return num
    return inner

@decorator
def show():
    print('哈哈')

@decorator
def getnum(x):
    return x

show()
print(getnum(3))
```

## 4 多个装饰器的使用
由内到外的一个装饰过程，先执行内部的装饰器，再执行外部的装饰器
```python
def make_div(func):
    print("make_div装饰器执行了")
    def inner():
        result = "<div>" + func() + "</div>"
        return result
    return inner

def make_p(func):
    print("make_p装饰器执行了")
    def inner():
        result = "<p>" + func() + "</p>"
        return result
    return inner

# 相当于make_div(make_p(show))
@make_div
@make_p
def show():
    return '哈哈'

print(show())


# 输出：
# make_p装饰器执行了
# make_div装饰器执行了
# <div><p>哈哈</p></div>
```

## 5 带有参数的装饰器
装饰器需要根据不同的参数来执行不同的装饰功能。由于语法糖形式的装饰器本身只能接收一个参数，因此需要在装饰器外面包裹一个函数。
```python
# 不能用语法糖的装饰器：自己琢磨的
def decorator(func, flag):
    def inner(*args, **kwargs):
        if flag == '+':
            print('执行了加法函数')
        if flag == '-':
            print('执行了减法函数')
        result = func(*args, **kwargs)
        return result
    return inner

def add_num(a, b):
    return a + b

def sub_num(a, b):
    return a - b

new_add_num = decorator(add_num, '+')
print(new_add_num(1, 2))
```
```python
# 用语法糖的装饰器：带参装饰器
def decorator_with_args(flag):
    def decorator(func):
        def inner(*args, **kwargs):
            if flag == '+':
                print('执行了加法函数')
            if flag == '-':
                print('执行了减法函数')
            result = func(*args, **kwargs)
            return result
        return inner
    return decorator

# 实际上decorator_with_args('+')是一个普通函数，返回值是一个装饰器。给返回值添加了@来调用装饰器装饰函数。
@decorator_with_args('+')   
def add_num(a, b):
    return a + b

@decorator_with_args('-')
def sub_num(a, b):
    return a - b

print(add_num(1, 2))
print(sub_num(1, 2))
```

## 6 类装饰器
* 通过定义一个类来修饰函数
* 通过类装饰函数后，如果要通过函数调用的方式来使用，类装饰器需要提供```__call__```方法

```python
class MyDecorator(object):
    def __init__(self, func):
        self.__func = func  # 设置为私有
    
    def __call__(self, *args, **kwargs):
        print('干得漂亮！')
        result = self.__func(*args, **kwargs)
        return result

@MyDecorator
def add_num(a, b):
    return a + b

@MyDecorator
def sub_num(a, b):
    return a - b

print(add_num(1, 2))
print(sub_num(1, 2))
```
