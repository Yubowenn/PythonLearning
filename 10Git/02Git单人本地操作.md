<!-- 让表格居中显示的风格 -->
<style>
.center 
{
  width: auto;
  display: table;
  margin-left: auto;
  margin-right: auto;
}
</style>


# 单人操作
使用Git提交文件到版本库有两步：

第一步：是使用 git add 把文件添加进去，实际上就是把文件添加到暂存区。

第二步：使用git commit提交更改，实际上就是把暂存区的所有内容提交到当前分支上。
## 1 单人主线操作

<div class="center">

指令|说明|拓展
:--:|:--:|:--:
|`git init`|把这个目录变成git可以管理的仓库，当前目录下会多了一个.git的空仓库
|`git config user.name 'yubowen'`|配置
|`git config user.email '123.qq.com'`|配置
|`git add`|指令将新内容添加到暂存区里面去|`git add login.py` => 追踪指定文件<br>`git add .` => 当前的所有文件都追踪
`git commit -m '说明'`|用命令告诉Git，把文件提交到仓库
`git commit -am '说明'`|提交合并指令
`git status`|查看是否还有文件未提交
`git log`|查看日志|`git log –pretty=oneline`=>查看一行日志

</div>


## 2 版本回退`git reset`指令

<div class="center">

指令|说明|拓展
:--:|:--:|:--:
|`git reset --hard HEAD^`|把当前的版本回退到上一个版本
|`git reset --hard HEAD~100`|回退到前100个版本
|`git reset --hard 版本号`|通过版本号回退
|`git reflog`|获取版本号

</div>

## 3 撤销工作区的代码
`git checkout -- file`（未提交暂存区之前）
命令 git checkout --file 意思就是，把file文件在工作区做的修改全部撤销，这里有2种情况，如下：
* file自动修改后，还没有放到暂存区，使用撤销修改就回到和版本库一模一样的状态。
* 另外一种是file已经放入暂存区了，接着又作了修改，撤销修改就回到添加暂存区后的状态。

## 4 撤销暂存区的代码
`git reset HEAD file`
暂存区代码 => 工作区代码。只是代码的位置发生了变化，此时文件中的内容并没有撤销。接下来如果要撤销工作区代码，则按上面的第3点来进行。
