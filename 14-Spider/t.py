from selenium import webdriver
import time

# 手动添加路径
driver = webdriver.Chrome()

url = "https://www.baidu.com"

# 司机开车了
driver.get(url)

# 让页面移到最下面点击加载，连续6次，司机会自动更新！！
print(driver.find_element_by_id('wrapper').text)