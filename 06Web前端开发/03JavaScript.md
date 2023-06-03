# JavaScript

JavaScript是运行在浏览器端的脚本语言，是由浏览器解释执行的，实现网页和用户的交互功能。

## 1 JS的引入方式
* 行内式
```html
<input type="button" name="" onclick="alert('OK!');">hello</div>
```
* 内嵌式
在```<head>```标签内加入```<style>```标签，在```<style>```标签内写CSS代码
```html
<script type="text/javascript">
    alert('OK!');
</script>
```
* 外链式
```html
<script type="text/javascript" src="js/index.js"></script>
<script>
    fnshow()
</script>
```
js文件：
```javascript
function fnshow(){
    alert("OK!")
}
```

## 2 变量和数据类型
JavaScript的语句应该以```;```结尾
### 2.1 定义变量
```var param = value```

### 2.2 数据类型
五种基本数据类型和一种复杂数据类型
* number 数字类型
* string 字符串类型
* boolean 布尔类型
* undefined 变量声明未初始化
* null 空对象 
* object 复合类型（对象）

## 3 获取标签元素
使用方法```document.getElementById```来获取页面上设置了```id```的元素，
* 示例1：```<div>```元素要写在JS代码的上面
```html
<div id="div1">Hello</div>

<script type="text/javascript">
    var oDiv = document.getElementByid('div1'); 
    alert(oDiv);
</script>
```

* 示例2：设置页面加载执行的函数，在执行函数里面获取标签元素
```html
<script type="text/javascript">
    window.onload = function(){
        var oDiv = document.getElementByid('div1'); 
    }
</script>

<div id="div1">Hello</div>
```

## 4 操作标签的属性
### 4.1 方法1
使用```document.getElementById```获取设置了```id```的元素之后，直接通过```.属性名```来获取对应属性的 属性值
* 操作```class```属性时，要写```.className```来获取
### 4.2 方法2
通过```innerHTML```来获取或设置标签包裹的内容
```html
<script type="text/javascript">
    window.onload = function(){
        var oDiv = document.getElementByid('div1');
        // 读取
        var sTxt = oDiv.innerHTML;
        alert(sTxt);
        // 写入
        oDiv.innerHTML = <a href="https://www.baidu.com">百度</a>
    }
</script>

<div id="div1">Hello</div> 
```

## 5 数组
### 5.1 数组的定义
```javascript
// 实例化对象创建
var aList = new Array(1,2,3);

// 字面量创建，推荐
var aList2 = [1,2,3,'asd'];
```

### 5.2 数组的操作
#### （1）获取数组长度
```javascript
var aList = [1,2,3,4,5]
alert(aList.length)
```
#### （2）根据下标添加和删除元素
```arr.splice(start, num, ele1,...,eleN);```
* start: 必需，开始删除的索引
* num: 可选，删除数组元素的数量
* elementN: 可选，在start索引处要插入的新元素

#### （3）追加元素
```arr.push(ele);```

#### （4）删除最后一个元素
```arr.pop();```，返回值是删除的元素

## 6 循环
### 6.1 for循环
```javascript
var arr = [1,2,3];
for(var index=0; index < arr.length; index++){
    var oValue = arr[index];
    alert(oValue);
}
```

### 6.2 while循环
```javascript
var arr = [1,2,3];

var index = 0
while(index < arr.length){
    var oValue = arr[index];
    alert(oValue);
    index++;
}
```

### 6.3 do...while循环
```javascript
var arr = [1,2,3];

var index = 0;
do{
    var oValue = arr[index];
    alert(oValue);
    index++;
}while(index < arr.length)

```

## 7 定时器
在一段特定的时间后执行某段代码
* 方法1：以指定时间间隔（毫秒计）调用一次函数
```javascript
setTimeout(func, delay, param1, param2, ...);
```
举例：
```javascript
function fnShow(name, age){
    alert("OK" + name + age);
    alert(tid);  //调用全局变量，不需要声明global
    clearTimeOut(tid);  //销毁定时器
}

var tid = setTimeOut(fnShow, 500, "里斯本", 20); //返回定时器的id
```
* 方法2：以指定时间间隔重复调用一个函数
```javascript
setInterval(func, delay, param1, param2, ...);
```


### 其他内容
* JS中```==```用来判断等于，```5=="5"```的结果是```true```。```===```用来判断全等。
* 比较运算符分别为```&& || !```。
* JS中不支持数组负下标
* 可以通过```console.log()```来输出内容
* 字符串拼接可以完成隐式类型转换


