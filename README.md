# Scraper Service

## Version 1.0

### 数据模型

第一版本，我们只使用 File 来存储数据，将重点放在网络和文件处理上

主要结构包括如下：

#### 图书分类/Category

* name 分类名称


#### 图书信息/Book

* name 图书名称
* cover 封面
* author 作者
* word_count 字数
* last_updat_time 最后更新时间 （可选）
* last_update_chapter 最后更新章节 （可选）
* desc 简介
* tags 标签


#### 图书资源/BookResource （可选）

* name 资源名称
* url 资源网址
* category 资源网址对应分类
* last_updat_time 资源网址对应最后更新时间 （可选）
* last_update_chapter 资源网址对应最后更新章节 （可选）


#### 图书章节/Chapter

* name 名称
* word_count 字数


#### 图书章节正文/ChapterContent

* content 正文


***在第一版本中，忽略不同源的概念，只要能抓取到章节内容即可***

### 元数据结构

因为我们第一版本不适用 DB，所以需要自己先设计一套元数据：

文件目录结构如下：

```
books/
  {category_id}/ # 分类 ID 作为目录
    .meta #目录对应的信息，如名称等

    {book_id}/ # 图书 ID 作为目录
      .meta #本书对应的元数据信息
      cover.jpg/png... #图书封面
      {chapter_1}.txt  #正文
      {chapter_2}.txt
      {chapter_3}.txt
      {chapter_4}.txt
      ...
      ...
```


META 可以以任何形式保存，如 json, properties, ini 等，选择你最喜欢的即可，如 JSON

```
{
  'name': '分类名称'
}
```


```
{
  'name': '图书名称',
  'cover': '封面图片地址', #你可以任意自己定义名称，在这里指明即可，如果没有说明，会尝试读取目录夹中叫 cover.png/jpg/gif 的文件
  'author': '作者',
  'word_count': '总字数',
  'last_updat_time': '最后更新时间',
  'last_update_chapter': '最后更新章节名称',
  'desc': '小说简介',
  'tags': '标签，以逗号或者分号间隔',
  'chapters': [ #章节列表
    {title: '章节标题名称1', updated_at: '更新时间', word_count: '本章节字数', id: '对应章节文件编号'}，
    {title: '章节标题名称2', updated_at: '更新时间', word_count: '本章节字数', id: '对应章节文件编号'}
  ]
}
```

## Version 2.0

将文件解析至 DB

## Version 3.0

提供 Web 在线浏览功能

## Version 4.0

提供手机客户端