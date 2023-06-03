# HTML

## 1 基本结构
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>网页标题</title>
    </head>
    <body>
        网页显示内容
    </body>
</html>
```
* ```<!DOCTYPE html>```是文档声明，指定页面使用的html版本，例子中声明了一个html5的网页；
* ```<head>...</head>```定义文档的头部，负责网页标题设置、编码格式、引入css和js。

## 2 常见html标签
* 双标签：允许嵌套
* 单标签
* 带属性标签
注：标签可以嵌套，但不能交叉嵌套

## 3 资源路径
* 资源路径一般写相对路径

## 4 列表标签
* 无序列表标签
```html
<ul>
    <li>content1</li>
    <li>content2</li>
</ul>
```

* 有序列表标签
```html
<ol>
    <li>content1</li>
    <li>content2</li>
</ol>
```

## 5 表格标签
* ```<table>```标签：表示表格
  * ```<tr>```标签：表示表格的一行
    * ```<td>```标签：表示表格中的列
    * ```<th>```标签：表示表格中的表头
```html
<table style="border: 1px solid black; border-collapse: collapse;">
    <tr>
        <th style="border: 1px solid black;">姓名</th>
        <th style="border: 1px solid black;">年龄</th>
    </tr>
    <tr>
        <td style="border: 1px solid black;">Tom</td>
        <td style="border: 1px solid black;">22</td>
    </tr>
</table>
```

## 6 表单标签```<form>```
### 6.1 标签介绍
标签|说明|备注
:--:|:--:|:--:
|```<form>```|定义整体的表单区域
|```<label>```|表单元素的文字标注标签，定义文字标注
|```<input>```|用户输入标签
|```<textarea>```|多行文本输入框
|```<select>```|下拉列表标签|与```<option>```组合使用

```<input>```标签的属性
属性|说明|备注
:--:|:--:|:--:
|```type="text"```|单行输入文本框
|```type="password"```|密码输入框
|```type="radio"```|单选框
|```type="checkbox"```|复选框
|```type="file"```|上传文件
|```type="submit"```|提交按钮
|```type="reset"```|重置按钮
|```type="button"```|普通按钮

注：换行的方式有两种：```<br>```标签；将内容放入```<p></p>```标签

### 6.2 表单提交
```<form>```标签的属性
属性|说明|备注
:--:|:--:|:--:
|```action```|表单数据提交地址
|```method```|提交的方式：GET和POST
其他表单元素的属性
属性|说明|备注
:--:|:--:|:--:
|```name```|表单元素的名称，即提交数据时的参数名
|```value```|表单元素的值，提交数据时参数名对应的值|一般用于不能输入的表单元素
注：GET方式提交后的键值以查询参数的形式提交给服务器，在地址栏呈现，并不安全。 因此提交隐私数据应该用POST方式
