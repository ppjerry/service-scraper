## 流程

我们主要采用 PR(Pull Request) 的模式来开发，按如下 Step By Step 来操作

### Fork 项目

访问项目地址：https://github.com/sjtu-cs/service-scraper 点击右方的 Fork 按钮，如下图

![Fork 代码](/dist/images/00-fork.png)

### 选择组织

如果你有组织，会提示选择哪个组织或个人账号

![Choose Org](/dist/images/01-choose-group.png)

请选择个人账号。如果没有，则直接 Fork成功。

### Fork 成功

你看到地址栏的地址变成了 https://github.com/${你的账号}/service-scraper， 如下图

![Forked](/dist/images/02-forked.png)

### Clone 代码到本地

你就可以 Clone 代码到本地进行开发了，按钮如下

![Clone](/dist/images/03-clone.png)

Clone 代码有两种方式协议，即分别如下：

* SSH
* HTTPS

推荐所有非 Win 的用户采用 SSH，Win 的用户随意，如果搞不定 SSH，就采用 HTTPS 协议。

Git for windows从这里下载

* https://git-for-windows.github.io/
* https://git-scm.com/download/win

随意，用你喜欢的就好，如第一个。

安装成功后，如果你对命令行不熟悉或不想看的话，可以进一步下载客户端，如：https://desktop.github.com/

如果安装这个成功后，点击上面截图中的 Clone or download 会显示 Open in Desktop，就是调用这个客户端。

如果你想专业一点，那么就打开你的 Terminal 使用 git clone 获取代码

```
git clone git://github.com/${你的账号}/service-scraper
```

或者

```
git clone https://github.com/${你的账号}/service-scraper
```

### 选择你喜欢的开发工具

获取成功后，切换到 service-scraper，用你喜欢的编辑器打开它即可。推荐一些编辑器，如：

* Sublime (Win/Linux/Mac)
* Atom （Win/Linux/Mac）
* TextMate (只有 Mac 平台)

当然还有一些重量级工具，如

* Pycharm (收费软件，注册机自行寻找)
* Eclipse (有基于 Eclise 做的插件，install 一个支持 Python 插件即可)

### 编写代码

在 src 目录下，新建以自己用户名的目录夹，然后以任务编号建立子目录，如下图

![文件目录](/dist/images/04-struct.png)

### 提交代码

编写完代码并测试通过后，就可以提交代码了。你可以使用上面提到的 Git Client 提交，也可以使用命令行提交，主要用到的命令如下


增加你操作的所有文件
```
git add src/${你的用户名}
```


Commit 到本地仓库

```
git commit -m '你本次提交的说明/注释'
```

Push 到远程仓库，即Github
```
git push
```
### Pull Request

访问你自己的项目，Github 会提示你 Pull Request

![提示 PR](/dist/images/05-pr-01.png)

点击后，如下

![提示 PR](/dist/images/05-pr-03.png)

注意代码从哪里到哪里合并，最下面是具体的文件变化。没有问题，点击那个绿色的 Create pull request得到如下界面

![提示 PR](/dist/images/05-pr-04.png)

默认信息是从你的 commit 信息中提取到的，你可以编辑，然后拉小伙伴来和你一起做 Code Review

至少要保证一到两个人来做 Code Review 才能最后合并代码

### Merge

最后没问题了，就将代码合并到项目中

![提示 PR](/dist/images/05-pr-05.png)


### 更多资料

* Git 快速入门： https://segmentfault.com/a/1190000000725599
* GitHub 快速入门-Git教程: http://www.jianshu.com/p/242ca1409b00
* Git 入门 PPT: http://rogerdudler.github.io/git-guide/index.zh.html
* Git教程: https://lvwzhen.gitbooks.io/git-tutorial/content/

网站资源很多，检索能找到很多的
