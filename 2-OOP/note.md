# 写在前面的话
- 跟出版社合作
    - [阅轩图书专营店-天猫](https://detail.tmall.com/item.htm?id=535882394166)
    - 推荐图书- [Python编程从入门到实践](https://login.tmall.com/?from=sm&redirect_url=https%3A%2F%2Fsec.taobao.com%2Fquery.htm%3Faction%3DQueryAction%26event_submit_do_login%3Dok%26smApp%3Dmalldetailskip%26smPolicy%3Dmalldetailskip-init-anti_Spider-checklogin%26smCharset%3DGBK%26smTag%3DMTAxLjU0LjE0Ny45MSwsYWViMzk4MTI1YTJmNDI0ZGFlYzZmNzhhMGY4Y2ExODk%253D%26captcha%3Dhttps%253A%252F%252Fsec.taobao.com%252Fquery.htm%26smReturn%3Dhttps%253A%252F%252Fdetail.tmall.com%252Fitem.htm%253Fid%253D535882394166%2526sm%253Dtrue%26smSign%3DPBDYu%252BZ%252FvpObeCd6aFRU9Q%253D%253D)
- 邮箱
    - 我们会教给大家用python发送邮件
    - 对邮箱进行设置，只要设置好了，通过邮箱地址和授权码就能发送邮件
    - 愿意的话可以联系 1320365896(qq)
- 下周一课程临时改用录制
- 下周三开始，前端课程并行开课

# 0. OOP-Python面向对象
- Python的面向对象
- 面向对象编程
    - 基础
    - 公有私有
    - 继承
    - 组合，Mixin
- 魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数
    
# 1. 面向对象概述（ObjectOriented，OO）
- OOP思想
    - 接触到任意一个任务，首先想到的是任务这个世界的构成，是由模型构成的
- 几个名词
    - OO:面向对象
    - OOA：面向对象的分析
    - OOD：面向对象的设计
    - OOI：xxx的实现
    - OOP：xxx的编程
    - OOA->OOD->OOI: 面向对象的实现过程
- 类和对象的概念
    - 类：抽象名词，代表一个集合，共性的事物
    - 对象：具象的事物，单个个体
    - 类跟对象的关系
        - 一个具象，代表一类事物的某一个个体
        - 一个是抽象，代表的是一大类事物
- 类中的内容，应该具有两个内容
    - 表明事物的特征，叫做属性(变量)
    - 表明事物功能或动作， 称为成员方法(函数)
   
# 2. 类的基本实现
- 类的命名
    - 遵守变量命名的规范
    - 大驼峰（由一个或者多个单词构成，每个单词首字母大写，单词跟单词直接相连）
    - 尽量避开跟系统命名相似的命名
- 你如何声明一个类
    - 必须用class关键字
    - 类由属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有纸，许使用None
    - 案例 01.py 
- 实例化类
    
        变量 = 类名() #实例化了一个对象
- 访问对象成员
    - 使用点操作符
    
             obj.成员属性名称
             obj.成员方法 
- 可以通过默认内置变量检查类和对象的所有成员
    - 对象所有成员检查
        
            # dict前后各有两个下划线
            obj.__dict__ 
    - 类所有的成员
        
            # dict前后各有两个下划线
           class_name.__dict__
    
    
          
# 3. anaconda基本使用
- anaconda主要是一个虚拟环境管理器
- 还是一个安装包管理器
- conda list： 显示anaconda安装的包
- conda env list:显示anaconda的虚拟环境列表
- conda create -n xxx python=3.6: 创建python版本为3.6的虚拟环境，名称为xxx