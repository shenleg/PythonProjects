import urllib


def unicode_escape_to_utf8(s):
    return s.encode("unicode_escape").decode("utf-8")


def url_encode(s):
    return urllib.parse.quote(s)
