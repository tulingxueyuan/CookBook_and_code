# 页面解析和数据提取
- 结构数据： 先有的结构，在谈数据
    - JSON文件
        - JSON Path
        - 转换成Python类型进行操作（json类）
    - XML文件
        - 转换成python类型（xmltodict）
        - XPath
        - CSS选择器
        - 正则
- 非结构化数据：先有数据，再谈结构
    - 文本
    - 电话号码
    - 邮箱地址
        - 通常处理此类数据，使用正则表达式
    - Html文件
        - 正则
        - XPath
        - CSS选择器
       
# 正则表达式
- 一套规则，可以在字符串文本中进行搜查替换等
- 案例v23,re的基本使用流程
- 案例v24，match的基本使用
- 正则常用方法：
    - match: 从开始位置开始查找，一次匹配
    - search：从任何位置查找，一次匹配， 案例v25
    - findall： 全部匹配，返回列表, 案例v26
    - finditer： 全部匹配，返回迭代器, 案例v26
    - split： 分割字符串，返回列表
    - sub：替换
- 匹配中文
    - 中文unicode范围主要在[u4e00-u9fa5]
    - 案例v27
    
- 贪婪与非贪婪模式
    - 贪婪模式： 在整个表达式匹配成功的前提下，尽可能多的匹配
    - 非贪婪模式： xxxxxxxxxxxxxxxxxxxxxx, 尽可能少的匹配
    - python里面数量词默认是贪婪模式
    - 例如：
        - 查找文本abbbbbbccc
        - re是 ab*
        - 贪婪模式： 结果是abbbbbb
        - 非贪婪： 结果是a
# XML
- XML(EXtensibleMarkupLanguage)   
-    http://www.w3school.com.cn/xml/index.asp
- 案例v28.xml
- 概念：父节点，子节点，先辈节点，兄弟节点，后代节点

# XPath
- XPath(XML Path Language), 是一门在XML文档中查找信息的语言，
- 官方文档： http://www.w3school.com.cn/xpath/index.asp
- XPath开发工具
    - 开元的XPath表达式工具： XMLQuire
    - chrome插件： Xpath Helper
    - Firefox插件： XPath CHecker
    
- 常用路径表达式：
    - nodename: 选取此节点的所有子节点
    - /: 从根节点开始选
    - //: 选取元素，而不考虑元素的具体为止
    - .:  当前节点
    - ..:父节点
    - @： 选取属性
    - 案例：
        - booksotre: 选取bookstore下的所有子节点
        - /booksotre: 选取根元素
        - booksotre/book: 选取bookstore的所有为book的子元素
        - //book: 选取book子元素
        - //@lang:选取名称为lang的所有属性
- 谓语(Predicates)
    - 谓语用来查找某个特定的节点，被向前在方括号中
    - /bookstore/book[1]: 选取第一个属于bookstore下叫book的元素
    - /bookstore/book[last()]: 选取最后一个属于bookstore下叫book的元素
    - /bookstore/book[last()-1]: 选取倒数第二个属于bookstore下叫book的元素
    - /bookstore/book[position()<3]: 选取属于bookstore下叫book的前两个元素
    - /bookstore/book[@lang]: 选取属于bookstore下叫book的,含有属性lang元素
    - /bookstore/book[@lang="cn"]: 选取属于bookstore下叫book的,含有属性lang的值是cn的元素
    - /bookstore/book[@price < 90]: 选取属于bookstore下叫book的,含有属性price的，且值小于90的元素
    - /bookstore/book[@price < 90]/title: 选取属于bookstore下叫book的,含有属性price的，且值小于90的元素的子元素title
    
- 通配符
    - `*` : 任何元素节点
    - @*： 匹配任何属性节点
    - node(): 陪陪任何类型的节点
- 选取多个路径
    - //book/tile  | //book/author : 选取book元素中的title和author元素
    - //tile | //price: 选取文档中所有的title和price元素
  
# lxml库
- python的HTML/XML的解析器
- 官方文档：   http://lxml.de/index.html
- 功能：
    - 解析HTML,案例v29.py
    - 文件读取，案例v30.html, v31.py
    - etree和XPath的配合使用, 案例v32.py

# CSS选择器  BeautifulSoup4
- 现在使用BeautifulSoup4
- http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
- 几个常用提取信息工具的比较：
    - 正则： 很快，不好用，不许安装
    - beautifulsoup：慢，使用简单，安装简单
    - lxml： 比较快，使用简单，安装一般
- 案例v33.py
- 四大对象
    - Tag
    - NavigableString
    - BeautifulSoup
    - Comment
- Tag
    - 对应Html中的标签
    - 可以通过soup.tag_name
    - tag两个重要属性
        - name
        - attrs
    - 案例a34  
 
- NavigableString
    - 对应内容值
  
- BeautifulSoup
    - 表示的是一个文档的内容，大部分可以把他当做tag对象
    - 一般我们可以用soup来表示
- Comment
    - 特殊类型的NavagableString对象， 
    - 对其输出，则内容不包括注释符号
- 遍历文档对象
    - contents: tag的子节点以列表的方式给出 
    - children： 子节点以迭代器形式返回 
    - descendants： 所子孙节点
    - string
    - 案例34
- 搜索文档对象
    - find_all(name, attrs, recursive, text, ** kwargs)  
        - name:按照那个字符串搜索，可以传入的内容为
            - 字符串
            - 正则表达式
            - 列表
        - kewwortd参数，可以用来表示属性
        - text： 对应tag的文本值
        - 案例34
            
- css选择器
    - 使用soup.select, 返回一个列表
    - 通过标签名称: soup.select("title")            
    - 通过类名： soup.select(".content")
    - id查找: soup.select("#name_id")
    - 组合查找: soup.select("div #input_content")
    - 属性查找: soup.select("img[class='photo'])
    - 获取tag内容： tag.get_text
    - 案例35