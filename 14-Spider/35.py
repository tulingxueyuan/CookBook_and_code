from urllib import request
from bs4 import BeautifulSoup


url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')


print(soup.prettify())

print("==" * 20)
titles = soup.select("title")
print(titles[0])


print("==" * 12)
metas = soup.select("meta[content='always']")
print(metas[0])


print("==" * 12)


