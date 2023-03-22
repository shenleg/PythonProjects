import re
import urllib.parse


def unicode_escape_to_utf8(s):
    return s.encode("unicode_escape").decode("utf-8")


def url_encode(s):
    return urllib.parse.quote(s, safe=":/?=&")


if __name__ == '__main__':
    # url = "http://127.0.0.1:5000/user?id=1&hobby=吃&hobby=drink"
    # print(urllib.parse.quote(url))
    # print(urllib.parse.urlparse(url))
    print("张".encode("utf-8"))
    print("张".encode("utf-16"))
