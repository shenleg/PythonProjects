import multiprocessing

import requests
import logging
import re
import json
import os

from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10

RESULT_DIR = "result"
os.path.exists(RESULT_DIR) or os.makedirs(RESULT_DIR)


def scrape_page(url):
    """根据url爬取网页返回网页内容"""
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error(f'get invalid status code {response.status_code} while scraping {url}')
    except requests.RequestException:
        logging.error(f'error occurred while scraping {url}', exc_info=True)


# def scrape_index(page):
#     """根据页码爬取索引页"""
#     index_url = f'{BASE_URL}/page/{page}'
#     return scrape_page(index_url)


def parse_index(html):
    """解析索引页，提取详情页url"""
    detail_pattern = re.compile(r'<a .*? href="(.*?)" class="name">')
    items = detail_pattern.findall(html)
    detail_urls = []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info(f"get detail url {detail_url}")
        detail_urls.append(detail_url)
    return detail_urls


def parse_detail(html):
    """解析详情页，获取想要的内容"""
    # 正则书写原则：1.前后标记辅助定位 2.内容辅助定位 3.独特内容定位 4.尽可能通用匹配不出错
    # re.S 匹配结果包含换行符
    cover_pattern = re.compile(r'<img.*?src="(.*?)".*?class="cover">', re.S)

    name_pattern = re.compile(r'<h2.*?>(.*?)</h2>', re.S)
    categories_pattern = re.compile(r'<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)
    publish_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})\s?上映', re.S)
    score_pattern = re.compile(r'<p.*?class="score.*?">(.*?)</p>', re.S)
    description_pattern = re.compile(r'<div.*?class="drama">.*?<p.*?>(.*?)</p>', re.S)
    cover = cover_pattern.search(html).group(1).strip() if cover_pattern.search(html) else None
    name = name_pattern.search(html).group(1).strip() if name_pattern.search(html) else None
    categories = categories_pattern.findall(html) if categories_pattern.findall(html) else []
    publish = publish_pattern.search(html).group(1).strip() if publish_pattern.search(html) else None
    score = score_pattern.search(html).group(1).strip() if score_pattern.search(html) else None
    description = description_pattern.search(html).group(1).strip() if description_pattern.search(html) else None
    return {
        "cover": cover,
        "name": name,
        "categories": categories,
        "publish": publish,
        "score": score,
        "description": description,
    }


def save_data(data):
    name = data.get("name")
    data_path = os.path.join(RESULT_DIR, name)
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def main():
    for i in range(1, TOTAL_PAGE + 1):
        # 获取索引页
        index_url = f"{BASE_URL}/page/{i}"
        index_html = scrape_page(index_url)
        # 解析索引页，获取详细页url
        detail_urls = parse_index(index_html)
        logging.info(f"detail_urls {detail_urls}")
        # 获取详细页
        for detail_url in detail_urls:
            detail_html = scrape_page(detail_url)
            # 解析详细页，获取数据
            data = parse_detail(detail_html)
            logging.info(f"get detail data {data}")
            save_data(data)


def main2(page):
    # 获取索引页
    index_url = f"{BASE_URL}/page/{page}"
    index_html = scrape_page(index_url)
    # 解析索引页，获取详细页url
    detail_urls = parse_index(index_html)
    logging.info(f"detail_urls {detail_urls}")
    # 获取详细页
    for detail_url in detail_urls:
        detail_html = scrape_page(detail_url)
        # 解析详细页，获取数据
        data = parse_detail(detail_html)
        logging.info(f"get detail data {data}")
        save_data(data)


if __name__ == '__main__':
    # main()
    # 把互不干扰的地方拆分，放到进程池加快执行
    pool = multiprocessing.Pool()
    pool.map(main2, range(1, TOTAL_PAGE + 1))
