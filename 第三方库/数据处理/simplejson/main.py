"""
Github：https://github.com/simplejson/simplejson
Doc：https://simplejson.readthedocs.io/en/latest/
"""

import simplejson as json


# Using Decimal instead of float
data = '{"value": 3.14159265358979323846264338327950288419716939937510}'
result = json.loads(data, use_decimal=True)  # 把 float 类型转换为 Decimal 类型
print(type(result['value']), result['value'])

d = json.dumps(result)  # dump 自动转换为字符串去除引号
print(d)
