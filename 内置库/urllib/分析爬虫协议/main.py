from urllib.robotparser import RobotFileParser

# 判断是否允许爬取
rp = RobotFileParser()
rp.set_url('https://www.baidu.com/robots.txt')
rp.read()
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/'))
print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))

# True
# False
# True
