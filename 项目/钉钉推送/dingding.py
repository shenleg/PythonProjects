import base64
import hashlib
import hmac
import time
import urllib.parse
import json

import requests

import jenkins


# jenkins
jenkins_url = "http://10.101.4.31:8080/jenkins"
jenkins_username = "zhangyunhui"
jenkins_password = "zhangyunhui123"
job_name = "onlyTestCanBuild-T01_Sampling"

# 钉钉推送
access_token = "f745709e26f3b96d7f936d06c97a3ad2a48faf6e470c41fb324df4f933c048d7"
secret = "SEC93e58a8805c5c1d54aa352110e54fef8d0ae24f7125a9f4685b1cb5308f07926"
# access_token = "0d982173c70c697aa3d5a5b93284e2f4adbce495944a3e1d966ab7833ff02672"  # 本机测试机器人
# secret = "SEC115ae302d2b6f25777d2ffdacd4eca3995e08667e5177934a96f3d4214892857"  # 本机测试机器人

jenkins_server = jenkins.Jenkins(jenkins_url, jenkins_username, jenkins_password)
job_url = jenkins_server.get_job_info(job_name)["url"]
job_last_build_url = jenkins_server.get_job_info(job_name)["lastBuild"]["url"]
report_url = job_last_build_url + "allure"


def dingding_send():
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

    url = 'https://oapi.dingtalk.com/robot/send?access_token={}&timestamp={}&sign={}'
    url = url.format(access_token, timestamp, sign)

    send_content = "## Pytest_Java_接口自动化脚本执行完成\n"
    with open("behaviors.json", "r", encoding="utf-8"
    ) as f:
        behaviors = json.load(f)
        for item in behaviors["items"]:
            title = f"### {item['name']} \n "
            total = f"#### 运行总数：{item['statistic']['total']} \n "  # 总数
            passed = f"#### 通过总数：{item['statistic']['passed']} \n "  # 通过数
            failed = f"#### 失败总数：{item['statistic']['failed']} \n "  # 未通过数
            broken = f"#### 异常总数：{item['statistic']['broken']} \n "  # 异常数
            passed_percent = f"#### 通过百分比：{(item['statistic']['passed'] / item['statistic']['total']) * 100:.2f}% \n "  # 百分比
            send_content += title + total + passed + failed + broken + passed_percent
        send_content += f"### 报告地址：\n{report_url}"

    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "自动化执行结果",
            "text": send_content
        }
    }
    requests.post(url, json=data)


if __name__ == '__main__':
    dingding_send()
