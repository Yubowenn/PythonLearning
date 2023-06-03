# logging日志

## 1 logging日志级别介绍
日志级别|说明
:--:|:--:|
|```DEBUG```|程序调试bug时使用
|```INFO```|程序正常运行时使用
|```WARNING```|程序未按预期运行时使用，但并不是错误，如:用户登录密码错误
|```ERROR```|程序出错误时使用，如:IO操作失败
|```CRITICAL```|特别严重的问题，导致程序不能再继续运行时使用，如:磁盘空间为空，一般很少使用
默认的是WARNING等级，当在WARNING或WARNING之上等级的才记录日志信息。日志等级从低到高的顺序是: DEBUG < INFO < WARNING < ERROR < CRITICAL

## 2 logging日志的使用
### 2.1 输出到控制台：
```python
import logging

logging.debug('这是一个debug级别的日志信息')
logging.info('这是一个info级别的日志信息')
logging.warning('这是一个warning级别的日志信息')
logging.error('这是一个error级别的日志信息')
logging.critical('这是一个critical级别的日志信息')

# 输出：
# WARNING:root:这是一个warning级别的日志信息
# ERROR:root:这是一个error级别的日志信息
# CRITICAL:root:这是一个critical级别的日志信息
```
```python
# 设置日志等级和输出日志格式
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logging.debug('这是一个debug级别的日志信息')
logging.info('这是一个info级别的日志信息')
logging.warning('这是一个warning级别的日志信息')
logging.error('这是一个error级别的日志信息')
logging.critical('这是一个critical级别的日志信息')

# 输出：
# 2019-02-13 20:41:33,080 - hello.py[line:6] - DEBUG: 这是一个debug级别的日志信息
# 2019-02-13 20:41:33,080 - hello.py[line:7] - INFO: 这是一个info级别的日志信息
# 2019-02-13 20:41:33,080 - hello.py[line:8] - WARNING: 这是一个warning级别的日志信息
# 2019-02-13 20:41:33,080 - hello.py[line:9] - ERROR: 这是一个error级别的日志信息
# 2019-02-13 20:41:33,080 - hello.py[line:10] - CRITICAL: 这是一个critical级别的日志信息
```
代码说明:
* level 表示设置的日志等级
* format 表示日志的输出格式, 参数说明:
  * %(levelname)s: 打印日志级别名称
  * %(filename)s: 打印当前执行程序名
  * %(lineno)d: 打印日志的当前行号
  * %(asctime)s: 打印日志的时间
  * %(message)s: 打印日志信息
### 2.2 保存到日志文件：
```python
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    filename="log.txt",
                    filemode="w")

logging.debug('这是一个debug级别的日志信息')
logging.info('这是一个info级别的日志信息')
logging.warning('这是一个warning级别的日志信息')
logging.error('这是一个error级别的日志信息')
logging.critical('这是一个critical级别的日志信息')
```
