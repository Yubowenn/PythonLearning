# with语句和上下文管理器

## 1 with语句的使用
* 写文件的危险写法：
```python
# 1、以读的方式打开文件
f = open("1.txt", "r")
# 2、读取文件内容
f.write("hello world")
# 3、关闭文件
f.close()


# 输出：
# Traceback (most recent call last):
#   File "/home/python/Desktop/test/xxf.py", line 4, in <module>
#     f.write("hello world")
# io.UnsupportedOperation: not writable
```
由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。

* try语句的写法：
```python
try:
    # 1、以读的方式打开文件
    f = open("1.txt", "r")
    # 2、读取文件内容
    f.write("xxxxx")

except IOError as e:
    print("文件操作出错", e)

finally:
    # 3、关闭文件
    f.close()


# 输出：
# 文件操作出错 not writable
```
这种方法虽然代码运行良好,但是缺点就是代码过于冗长。

* with语句的写法：
```python
# 1、以写的方式打开文件
with open("1.txt", "w") as f:
    # 2、读取文件内容
    f.write("hello world")
```
with语句执行完成以后自动调用关闭文件操作，即使出现异常也会自动调用关闭文件操作。


## 2 上下文管理器
一个类只要实现了```__enter__()```和```__exit__()```这个两个方法，通过该类创建的对象我们就称之为上下文管理器。```open()```函数就是一个上下文对象
* 示例：定义一个File类，实现 ```__enter__()``` 和 ```__exit__()```方法，然后使用 with 语句来完成操作文件
```python
class File(object):

    # 初始化方法
    def __init__(self, file_name, file_model):
        # 定义变量保存文件名和打开模式
        self.file_name = file_name
        self.file_model = file_model

    # 上文方法
    def __enter__(self):
        print("进入上文方法")
        # 返回文件资源
        self.file = open(self.file_name,self.file_model)
        return self.file

    # 下文方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("进入下文方法")
        self.file.close()


if __name__ == '__main__':

    # 使用with管理文件
    with File("1.txt", "r") as file:
        file_data = file.read()
        print(file_data)


# 输出：
# 进入上文方法
# hello world
# 进入下文方法
```

## 3 上下文管理器的另一种实现方式
假如想要让一个函数成为上下文管理器，Python 还提供了一个 ```@contextmanager``` 的装饰器，更进一步简化了上下文管理器的实现方式。通过 ```yield``` 将函数分割成两部分，yield 上面的语句在 ```__enter__``` 方法中执行，yield 下面的语句在 ```__exit__``` 方法中执行，紧跟在 ```yield``` 后面的参数是函数的返回值。
```python
# 导入装饰器
from contextlib import contextmanager


# 装饰器装饰函数，让其称为一个上下文管理器对象
@contextmanager
def my_open(path, mode):
    try:
        # 打开文件
        file = open(file_name, file_mode)
        # yield之前的代码好比是上文方法
        yield file
    except Exception as e:
        print(e)
    finally:
        print("over")
        # yield下面的代码好比是下文方法
        file.close()

# 使用with语句
with my_open('out.txt', 'w') as f:
    f.write("hello , the simplest context manager")
```

