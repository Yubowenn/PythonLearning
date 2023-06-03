# ajax（Asynchronous JavaScript and XML）
ajax是一个前后台配合的技术，可以让javascript发送异步的http请求，与后台通信进行数据的获取。最大的优点是局部刷新。即当前端页面要和后端服务器进行数据交互就可以使用ajax。

## 1 ajax的使用
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
        // 向web服务器发送ajax请求，本质上是一个http请求
        $.ajax({
            // 请求资源的地址，如果不指定ip地址和端口号，默认是请求自己服务器的资源
            url: "data.json",
            // 请求方式：GET、POST
            type: "GET",
            // 指定对服务器数据的解析格式
            dataType: "JSON",
            // data表示发送给web服务器的参数，这里没有展示
            success: function(data){
                console.log(data);
            },  
            error: function(){

            },
            // 是否使用异步请求
            async: true
        });
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
* 发送GET请求的ajax简写方式：

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
        // 1. url
        // 2. 请求传给web服务器的参数
        // 3. success()
        // 4. 返回数据的解析方式
        $.get("data.json", {"name": "tom"}, function(data){
            alert(data.name);
        }, "JSON").error(function(){
            alert("请求失败");
        });
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