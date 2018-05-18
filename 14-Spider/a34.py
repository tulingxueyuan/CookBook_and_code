from urllib import request
from bs4 import BeautifulSoup


url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')


print("==" * 12)
tags = soup.find_all(re.compile('^me'), content="always")
for tag in tags:
    print(tag)
print("==" * 12)

