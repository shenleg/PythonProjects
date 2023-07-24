from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get(r'https://www.baidu.com')

logo = browser.find_element(By.CLASS_NAME, 'index-logo-srcnew')
print(logo.id)
print(logo.location)  # 页面位置
print(logo.tag_name)
print(logo.size)
print(logo.rect)  # size 和 location 结合
print(logo.tag_name)

browser.close()