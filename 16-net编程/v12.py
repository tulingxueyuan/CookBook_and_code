# 导入相关包
# poplib负责从MDA到MUA下载
import poplib

# 以下包负责相关邮件结构解析
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# 得到邮件的原始内容
# 这个过程主要负责从MDA到MUA的下载并使用Parse粗略解析
def getMsg():
    # 准备相应的信息
    email = "1366798119@qq.com"
    # 邮箱的授权码
    pwd = "hjpovygcxmrshhcj"

    # pop3服务器地址
    pop3_srv = "pop.qq.com" # 端口995

    # ssl代表是安全通道
    srv = poplib.POP3_SSL(pop3_srv)

    # user代表email地址
    srv.user(email)
    # pass_代表密码
    srv.pass_(pwd)

    # 以下操作根据具体业务具体使用
    # stat返回邮件数量和占用空间
    # 注意stat返回一个tuple格式
    msgs, counts = srv.stat()
    print("Messages: {0}, Size: {1}".format(msgs, counts))

    # list返回所有邮件编号列表
    # mails是所有邮件编号列表
    rsp, mails, octets = srv.list()
    # 可以查看返回的mails列表类似[b'1 82923', b'2 2184', ...]
    print(mails)


    # 获取最新一封邮件，注意，邮件索引号是从1开始, 最新代表索引号最高
    index = len(mails)
    # retr负责返回一个具体索引号的一封信的内容，此内容不具有可读性
    # lines 存储邮件的最原始文本的每一行
    rsp, lines, octets = srv.retr(index)

    # 获得整个邮件的原始文本
    msg_count = b'\r\n'.join(lines).decode("utf-8")
    # 解析出邮件整个结构体
    # 参数是解码后的邮件整体
    msg = Parser().parsestr(msg_count)

    #关闭链接
    srv.quit()

    return msg


# 详细解析得到的邮件内容
# msg代表是邮件的原始内容
# idnent代表的是邮件嵌套的层级
def parseMsg(msg, indent=0):
    '''
    1. 邮件完全可能是有嵌套格式
    2. 邮件只有一个From，To，Subject之类的信息

    :param msg:
    :param indent: 描述邮件里面有几个邮件MIMEXXX类型的内容,展示的时候进行相应缩进
    :return:
    '''

    # 想办法提取出头部信息
    # 只有在第一层的邮件中才会有相关内容，
    # 此内容只有一个
    if indent == 0:
        for header in ['From', "To", 'Subject']:
            # 使用get可以避免如果没有相关关键字报错的可能性
            # 如果没有 关键字”From“， 我们使用 msg["From"]会报错
            value = msg.get(header, '')
            if value:
                # Subject中的内容直接解码就可以，他是字符串类型
                if header == 'Subject':
                    value = decodeStr(value)
                # 如果是From和To字段，则内容大概是 "我的邮箱<xxxxx@qq.com>“这种格式
                else:
                    hdr, addr = parseaddr(value)
                    name = decodeStr(hdr)
                    # 最终返回形如  "我的邮箱<xxx@qq.com>的格式
                    value = "{0}<{1}>".format(name, addr)
            print("{0}, {1}: {2}".format(indent, header, value))

    # 下面代码关注邮件内容本身
    # 邮件内容中，有可能是multipart类型，也有可能是普通邮件类型
    # 下面的解析使用递归方式
    if (msg.is_multipart()):
        # 如果是multipart类型，则调用递归解析

        # 得到多部分邮件的一个基础邮件部分
        parts = msg.get_payload()
        # enumerate 函数是内置函数
        # 作用是将一个列表，此处是parts，生成一个有索引和parts原内容构成的新的列表
        # 例如 enumerate(['a', 'b', 'c']) 结果是:  [(1,'a'), (2, 'b'), (3, 'c')]
        for n,part in enumerate(parts):
            # 一个字符串乘以一个数字的意思是对这个字符串进行n倍扩展
            # 比如 ”aa" * 2 -> "aaaa"
            print("{0}spart: {1}".format(' '*indent, n))
            parseMsg(part, indent+1)
    else: # 基础类型
        # get_content_type是系统提供函数，得到内容类型
        content_type = msg.get_content_type()
        # text/plain 或者 text/html是固定值
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guessCharset(msg)
            if charset:
                content = content.decode(charset)
            print("{0}Text: {1}".format(indent, content))

        else: #不是文本内容，则应该是附件
            print('{0}Attachment: {1}'.format(indent, content_type))

def decodeStr(s):
    '''
    s代表一封邮件中From，To，Subject中的任一项
    对s进行解码，解码是编码的逆过程
    :param s:
    :return:
    '''
    value, charset = decode_header(s)[0]
    # charset完全可能为空
    if charset:
        # 如果指定编码，则用指定编码格式进行解码
        value = value.decode(charset)

    return value

def guessCharset(msg):
    '''
    猜测邮件的编码格式
    :param msg:
    :return:
    '''
    # 调用现成的函数
    charset = msg.get_charset()

    if charset is None:
        # 找到内容类型，并转换成小写
        content_type = msg.get("Content-Type", "").lower()
        pos = content_type.find("charset=")
        if pos >= 0:
            # 如果包含chraset，则内容形如 charset=xxxx
            charset = content_type[pos+8:].strip()

    return  charset




if __name__ == "__main__":
    # 得到邮件的原始内容
    msg = getMsg()
    print(msg)
    # 精确解析邮件内容
    parseMsg(msg, 0)
