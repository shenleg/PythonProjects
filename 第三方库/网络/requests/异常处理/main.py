import traceback

import requests
from requests import RequestException


def send_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
        result = response.json()  # 假设服务器返回的是JSON格式的数据
        if result["code"] != 200:
            raise Exception("请求失败，返回结果异常")
        return result
    except RequestException as e:
        print(f"请求错误，异常类型：{type(e)}，错误信息: {e}")
        traceback.print_exc()
        return None


if __name__ == "__main__":
    url = "http://127.0.0.1:5000/data"
    res = send_request(url)
    print(res)
