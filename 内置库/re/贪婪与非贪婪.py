import re

# 贪婪匹配，尽可能匹配多的字符
content = "Hello 1234567 World This is a Regex demo"
result = re.match(r"^Hello.*(\d+).*demo$", content)
print(result.group(1))

# 非贪婪匹配，尽可能匹配少的字符
content = "Hello 1234567 World This is a Regex demo"
result = re.match(r"^Hello.*?(\d+).*demo$", content)
print(result.group(1))

# 结论：
# 1.字符串中间尽量使用非贪婪匹配
# 2.字符串结尾使用贪婪匹配
