# JQuery
JQuery是对JavaScript的一个封装

## 1 jQuery的引入
```html
<script src="js/jquery-1.12.4.min.js"></script>
```
 
## 2 jQuery选择器
### 2.1 选择器
示例|说明
:--:|:--:
|```$('#mId')```|选择id为mId的标签
|```$('.mClass')```|选择class为mClass的标签
|```$('li')```|选择所有的```<li>```标签
|```$('#ul1 li span')```|选择id为ul1的标签下的所有li标签下的span标签
|```$('input[name=first]')```|选择name属性为first的input标签
### 2.2 选择集过滤
* has方法：选取包含指定选择器的标签
```html
<script>
    $(function{
        // has方法
        var $div = $("div").has("#mytext");
        // 设置样式
        $div.css({"background": "red"});
    })
</script>
```
* eq方法：选取指定索引的标签 

### 2.3 选择集转移
以选择的标签为参照，获取转移后的标签
示例|说明
:--:|:--:
|```$('#box').prev()```|选择id为box元素的上一个同级元素
|```$('#box').prevAll()```|选择id为box元素的上面所有元素
|```$('#box').next()```|
|```$('#box').nextAll()```|
|```$('#box').parent()```|选择id为box元素的父元素
|```$('#box').siblings()```|选择id为box元素的所有子元素
|```$('#box').prev()```|选择id为box元素的其他同级元素
|```$('#box').find('.myClass')```|选择id为box元素下的class为myClass的元素


### 2.4 获取和设置元素的内容
```javascript
var $div = $("#div1");

var result = $div.html();   //获取标签的html内容

$div.html("<span style='color:red'>hello</span>");  //设置

$div.append("<span style='color:green'>hi</span>"); //追加
```

### 2.5 获取和设置元素的属性
* 样式属性用```.css```，其他属性用```.prop()```
* value属性可以用```$text.prop("value")```或```$text.val()```

## 3 jQuery事件
事件|说明
:--:|:--:
|```click()```|鼠标单击
|```blur()```|元素失去焦点
|```focus()```|元素获得焦点
|```mouseover()```|鼠标进入（进入子元素也触发）
|```mouseout()```|鼠标离开（离开子元素也触发）
|```ready()```|DOM加载完成
* 举例：点击li标签时，标签内容会变为红色
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="js/jquery-1.12.4.min.js"></script>
    <script>
        // 等页面加载完成后获取标签元素
        // $(document).ready(function(){

        // });

        $(function(){
            var $lis = $("ul li");

            $lis.click(function(){
                // this.style.color = "red";   // 原生js写法
                $(this).css({"color": "red"});  // jquery写法
                alert($(this).index())
            });
        })
    </script>
</head>
<body>
    <ul>
        <li>apple</li>
        <li>pear</li>
        <li>ballana</li>
    </ul>
</body>
</html>
```

## 4 事件代理
利用事件冒泡（子元素触发后，默认会向上级传递）的原理，将事件加到父级上。通过判断时间来源，执行相应的子元素的操作。目的是提高复用性。
```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="js/jquery-1.12.4.min.js"></script>
    <script>
        $(function(){
            var $ul = $("ul");

            $ul.delegate("li", "click", function(){
                $(this).css({"color": "red"});
            });
        })
    </script>
</head>
<body>
    <ul>
        <li>apple</li>
        <li>pear</li>
        <li>ballana</li>
    </ul>
</body>
</html>
```

## 5 JavaScript对象
### 5.1 对象创建
* 通过顶级Object对象实例化一个对象
```html
<script>
    var person = new Object();

    // 添加属性
    person.name = "Tom";

    // 添加方法
    person.sayName = function(){
        alert(this.name);
    }

    // 调用属性和方法
    alert(person.name);
    person.sayName()
</script>
```
* 通过对象字面量创建

```html
<script>
    var person = {
        // 添加属性
        name: "Tom",
        // 添加方法
        sayName: sfunction(){
            alert(this.name);
        }
    };

    // 调用属性和方法
    alert(person.name);
    person.sayName()
</script>
```

## 6 JSON（JavaScript Object Notation）
### 6.1 格式
类似于JavaScript对象的字符串，json有两种格式：
* 对象格式
```json
{
    "name": "Tom",
    "age": 10,
}
```
json中的key以及字符串值需要用双引号。
* 数组格式
```json
["Tom", 18, "programmer"]
```
实际过程中的json数据比较复杂，是二者的混合使用。
### 6.2 json数据转换成JavaScript对象
```javascript
var sJson = '[{"name": "tom", "age":10}, {"name": "jerry", "age":3}]'; 
var aArray = JSON.parse(sJson);
var oPerson = aArray[1]; //通过下标访问指定js对象

// 操作属性
alert(oPerson.name);
alert(oPerson.age);
```
注：Python服务器可以将json数据解析成字典或列表 








