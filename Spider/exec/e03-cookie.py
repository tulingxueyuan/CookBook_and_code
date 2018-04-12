'''
登录开心网
利用cookie
免除ssl
'''
from urllib import request, parse
import ssl
'''
步骤：
1， 寻找登录入口， 通过搜查相应文字可以快速定位
  login_url = "https://security.kaixin001.com/login/login_post.php"
  相应的用户名和密码对应名称为email, password
2. 构造opener
3. 构造login函数
'''

import ssl
# 忽略安全问题
ssl._create_default_https_context = ssl._create_unverified_context

from http import cookiejar

cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler, https_handler, cookie_handler)



def login():

    login_url = "https://security.kaixin001.com/login/login_post.php"

    data = {
        "email":"13119144223",
        "password": "123456"
    }


    # 对post的data内容进行编码
    data = parse.urlencode(data)

    # http协议的请求头
    headers = {
        "Content-Length": len(data),
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
    }

    # 构造请求Request对象
    # data要求是一个bytes对象，所以需要进行编码
    req = request.Request(login_url, data=data.encode(), headers=headers)

    rsp = opener.open(req)

    html = rsp.read()
    html = html.decode()

def getHomePage():
    base_url = "http://www.kaixin001.com/home/?_profileuid=181697221"

    rsp = opener.open(base_url)
    html = rsp.read()
    html = html.decode()

    print(html)

if __name__ == '__main__':
    login()
    getHomePage()