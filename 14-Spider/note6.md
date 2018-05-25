# 分布式爬虫
- 单机爬虫的问题：
    - 单机效率
    - IO吞吐量
- 多爬虫问题
    - 数据共享
    - 在空间上不同的多台机器，可以成为分布式
- 需要做：
    - 共享队列
    - 去重
- Redis
    - 内存数据库
    - 同时可以落地保存到硬盘
    - 可以去重
    - 可以把他理解成一共dict，set，list的集合体  
    - 可以对保存的内容进行生命周期控制 
    
- 内容保存数据库
    - MongoDB
    - Mysql等传统关系数据库
  
- 安装scrapy_redis
    - pip install scrapy_reids
    - github.com/rolando/scrapy-redis
    - scrapy-redis.readthedocs.org
    
# 推荐书籍
- Python爬虫开发与项目实战， 范传辉， 机械工业出版社
- 精通 python爬虫框架scrapy, 李斌 翻译， 人民邮电出版社
- 崔庆才， 