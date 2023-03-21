def unicode_escape_to_utf8(s):
    print("hh", s)
    return s.encode("unicode_escape").decode("utf-8")
