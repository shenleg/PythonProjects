import base64
import hashlib
import hmac
import re
import subprocess
import time
import urllib.parse
import json
import urllib3

from sqlalchemy import create_engine, text

# SQLAlchemy connect info
host = '10.101.4.31'
port = 3306
db = 'so_auto_comp'
user = 'test'
password = 'test'

url = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(user, password, host, port, db)

engine = create_engine(url)



def DingTalkSend(status_code, content):
    # 钉钉推送
    timestamp = str(round(time.time() * 1000))
    # secret = 'SEC115ae302d2b6f25777d2ffdacd4eca3995e08667e5177934a96f3d4214892857'  # 本机测试机器人
    secret = 'SEC93e58a8805c5c1d54aa352110e54fef8d0ae24f7125a9f4685b1cb5308f07926'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

    url = 'https://oapi.dingtalk.com/robot/send?access_token={}&timestamp={}&sign={}'
    # url = url.format("0d982173c70c697aa3d5a5b93284e2f4adbce495944a3e1d966ab7833ff02672", timestamp, sign)  # 本机测试机器人
    url = url.format("f745709e26f3b96d7f936d06c97a3ad2a48faf6e470c41fb324df4f933c048d7", timestamp, sign)

    if status_code == 0:
        res_text = "成功"
    else:
        res_text = "失败"

    local_ip = re.search(r"local_ip=([\d\\.]*)", content).group(1)
    db_name = re.search(r"db_name=([\w-]*)", content).group(1)
    back_file_path = re.search(r"back_file_path=([\w/\-\\.]*)", content).group(1)
    
    # 查询数据库
    table_info = ""
    with engine.connect() as con:
        res = con.execute(text("show tables")).all()
        for table in [i[0] for i in res]:
            res = con.execute(text(f"select count(*) from `{table}`")).all()
            table_info += f"\n备份表 {table} 共 {res[0][0]} 条数据"
    

    con = {"msgtype": "text",
           "text": {
               "content": "数据库备份完成。"
                          f"\n执行结果：{res_text}"
                          f"\n备份服务器：{local_ip}"
                          f"\n备份数据库：{db_name}"
                          + table_info +
                          f"\n备份文件路径：{back_file_path}"
                          
                }
           }
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    jd = json.dumps(con)
    jd = bytes(jd, 'utf-8')
    http.request('POST', url, body=jd, headers={'Content-Type': 'application/json'})


if __name__ == '__main__':
    res = subprocess.getstatusoutput("sh /home/guosheng/db_backup/db_backup.sh")
    print("命令执行状态\n", res[0])
    print("命令执行结果\n", res[1])
    DingTalkSend(res[0], res[1])
    

