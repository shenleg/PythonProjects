from urllib.parse import urlparse

# urlparse()方法将url解析成6个部分，分别是scheme、netloc、path、params、query、fragment
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result, sep="\n")
# <class 'urllib.parse.ParseResult'>
# ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
print(result.scheme, result[0], result.netloc, result[1], sep="\n")
# https
# https
# www.baidu.com
# www.baidu.com

