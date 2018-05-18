
'''
破解有道词典
V1
'''

from urllib import request, parse


def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = {
        "i": "boy",
        "from":"AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1523100789519",
        "sign": "b8a55a436686cd89873fa46514ccedbe",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult": "false"
    }

    # 参数data需要是bytes格式
    data = parse.urlencode(data).encode()

    headers = {
                  "Accept": "application/json,text/javascript,*/*;q=0.01",
                  #"Accept-Encoding": "gzip,deflate",
                  "Accept-Language": "zh-CN,zh;q=0.9",
                  "Connection": "keep-alive",
                  "Content-Length": "200",
                  "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                  "Cookie": "OUTFOX_SEARCH_USER_ID=-1548144101@10.168.8.76;JSESSIONID=aaaTLWzfvp5Hfg9mAhFkw;OUTFOX_SEARCH_USER_ID_NCOO=1999296830.4784973;___rl__test__cookies=1523100789517",
                  "Host": "fanyi.youdao.com",
                  "Origin": "http://fanyi.youdao.com",
                  "Referer": "http://fanyi.youdao.com/",
                  "User-Agent": "Mozilla/5.0( X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36 X-Requested-With: XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao("boy")
