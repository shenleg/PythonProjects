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

import hashlib


def get_file_md5(file_path):
    """获取文件的md5值
    :param file_path: str，文件路径
    :return: str，文件的md5值
    """
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
        return md5_hash.hexdigest()