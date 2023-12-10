from urllib.parse import urlsplit

# urlsplit()方法将url解析成5个部分，分别是scheme、netloc、path(param合并)、query、fragment
result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result, sep="\n")
# <class 'urllib.parse.SplitResult'>
# SplitResult(scheme='https', netloc='www.baidu.com', path='/index.html;user', query='id=5', fragment='comment')
print(result.scheme, result[0], result.netloc, result[1], sep="\n")
# https
# https
# www.baidu.com
# www.baidu.com
