# 网络编程
- 网络：
- 网络协议： 一套规则
- 网络模型：
    - 七层模型-七层
        - 物理层
        - 数据链路层
        - 网络层
        - 传输层
        - 会话层
        - 表示层
        - 应用层
    - 四层模型-实际应用
        - 链路层
        - 网络
        - 传输层
        - 应用层
        
- 每一层都有相应的协议负责交换信息或者协同工作
- TCP/IP 协议族
- IP地址：负责在网络上唯一定位一个机器
    - IP地址分ABCDE类
    - 是由四个数字段组成，每个数字段的取值是0-255
    - 192.168.xxx.xxx:局域网ip
    - 127.0.0.1：本机
    - IPv4, IPv6
    
- 端口
    - 范围： 0-65535
        - 知名端口：0-1023
        - 非知名端口：1024-
        
# TCP/UDP协议
- UDP：非安全的不面向链接的传输
    - 安全性差
    - 大小限制64kb
    - 没有顺序
    - 速度快
- TCP
    - 基于链接的通信
    
- SOCKET编程
    - socket（套接字）: 是一个网络通信的端点， 能实现不同主机的进程通信，网络大多基于Socket通信
    - 通过IP+端口定位对方并发送消息的通信机制
    - 分为UDP和TCP
    - 客户端Client： 发起访问的一方
    - 服务器端Server：接受访问的一方
- UDP 编程
    - Server端流程
            1. 建立socket，socket是负责具体通信的一个实例
            2. 绑定，为创建的socket指派固定的端口和ip地址
            3. 接受对方发送内容
            4. 给对方发送反馈，此步骤为非必须步骤
    - Client端流程
            1. 建立通信的socket
            2. 发送内容到指定服务器
            3. 接受服务器给定的反馈内容
    - 服务器案例v01
    - 客户端案例v02
    - 服务器程序要求永久运行，一般用死循环处理
    - 改造的服务器版本v03
    
- TCP编程
    - 面向链接的传输，即每次传输之前需要先建立一个链接
     - 客户端和服务器端两个程序需要编写
     - Server端的编写流程
         1. 建立socket负责具体通信，这个socket其实只负责接受对方的请求，真正通信的是链接后从新建立的socket
         2. 绑定端口和地址
         3. 监听接入的访问socket
         4. 接受访问的socket，可以理解接受访问即建立了一个通讯的链接通路
         5. 接受对方的发送内容，利用接收到的socket接收内容
         6. 如果有必要，给对方发送反馈信息
         7. 关闭链接通路
     - Client端流程
          1. 建立通信socket
          2. 链接对方，请求跟对方建立通路
          3. 发送内容到对方服务器
          4. 接受对方的反馈
          5. 关闭链接通路
     - 案例v04， v05
     
# FTP编程
- FTP(FileTransferProtocal)文件传输协议
- 用途： 定制一些特殊的上传下载文件的服务
- 用户分类： 登陆FTP服务器必须有一个账号
    - Real账户: 注册账户
    - Guest账户： 可能临时对某一类人的行为进行授权
    - Anonymous账户： 匿名账户，允许任何人
- FTP工作流程
    1. 客户端链接远程主机上的FTP服务器
    2. 客户端输入用户名和密码（或者“anonymous”和电子邮件地址）
    3. 客户端和服务器进行各种文件传输和信息查询操作
    4. 客户端从远程FTP服务器退出，结束传输   
    
- FTP文件表示
    - 分三段表示FTP服务器上的文件
    - HOST: 主机地址，类似于 ftp.mozilla.org, 以ftp开头
    - DIR：目录， 表示文件所在本地的路径，例如 pub/android/focus/1.1-RC1/ 
    - File： 文件名称， 例如 Klar-1.1-RC1.apk
    - 如果想完整精确表示ftp上某一个文件，需要上述三部分组合在一起
    - 案例v06
    
# Mail编程
## 电子邮件的历史
- 起源
    - 1969 Leonard K. 教授发给同时的 “LO”
    - 1971 美国国防部自主的阿帕网(Arpanet)的通讯机制
    - 通讯地址里用@， 
    - 1987年中国的第一份电子邮件  
    “Across the Great Wall we can reach every corner in the world"

- 管理程序
    - Euroda使邮件普及 
    - Netscape，outlook，forxmail后来居上
    - Hotmal使用浏览器发送邮件i
- 参考资料
    - [官网](https://docs.python.org/3/library/email.mime.html)
    
## 邮件工作流程
- MUA(MailUserAgent)邮件用户代理
- MTA(MailTransferAgent)邮件传输代理
- MDA(MailDeliveryAgent)邮件投递代理
- laoshi@qq.com, 老师，北京海淀
- xuesheng@sina.com, 学生，上海江岸区
- 流程
    1. MUA->MTA, 邮件已经在服务器上了
    2. qq MTA->.........->sina MTA, 邮件在新浪的服务器上
    3. sina MTA-> sina MDA, 此时邮件已经在你的邮箱里了
    4. sina MDA -> MUA(Foxmail/Outlook), 邮件下载到本地电脑
   
- 编写程序
    - 发送：  MUA->MTA with SMTP:SimpleMailTransferProtocal，包含MTA->MTA
    - 接受：  MDA->MUA with POP3 and IMAP：PostOfficeProtocal v3 and  InternetMessageAccessProtocal v4
    
- 准备工作
    - 注册邮箱（以qq邮箱为例）
    - 第三方邮箱需要特殊设置， 以qq邮箱为例
        - 进入设置中心
        - 取得授权码
        
- Python for mail
    - SMTP协议负责发送邮件
        - 使用email模块构建邮件
            - 纯文本邮件
            - 案例v07
        - HTML格式邮件发送
            - 准备HTML代码作为内容
            - 把邮件的subtpye设为html
            - 发送
            - 案例v08
        - 发送带附件的邮件
            - 可以把邮件看作是一个文本邮件和一个附件的合体
            - 一封邮件如果涉及多个部分，需要使用MIMEMultipart格式构建
            - 添加一个MIMEText正文
            - 添加一个MIMEBase或者MEMEText作为附件
            - 案例v09
            
        - 添加邮件头， 抄送等信息
            - mail["From"] 表示发送着信息，包括姓名和邮件
            - mail["To"]  表示接收者信息，包括姓名和邮件地址
            - mail["Subject"] 表示摘要或者主题信息
            - 案例v10
        - 同时支持html和text格式
            - 构建一个MIMEMultipart格式邮件
            - MIMEMultipart的subtype设置成alternative格式
            - 添加HTML和text邮件
            - 案例v11
        
        - 使用smtplib模块发送邮件
    
    - POP3协议接受邮件 
        - 本质上是MDA到MUA的一个过程
        - 从 MDA下载下来的是一个完整的邮件结构体，需要解析才能得到每个具体可读的内容
        - 步骤：
            1. 用poplib下载邮件结构体原始内容
                1. 准备相应的内容（邮件地址，密码，POP3实例）
                2. 身份认证
                3. 一般会先得到邮箱内邮件的整体列表
                4. 根据相应序号，得到某一封信的数据流
                5. 利用解析函数进行解析出相应的邮件结构体
            2. 用email解析邮件的具体内容
        - 案例v12
