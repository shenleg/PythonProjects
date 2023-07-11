import difflib

"""
'-'    第1个序列中出现
'+'    第2个序列中出现
' '    两行相同
'?'    增量差异
"""

a = """
abc
s
sd
"""

b = """
ab
xc
"""

d = difflib.Differ()
res = d.compare(a, b)
print("".join(list(res)))
