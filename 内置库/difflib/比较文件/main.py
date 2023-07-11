import difflib

with open("a.txt", encoding="utf-8") as f:
    file1_contents = f.read().splitlines()
with open("b.txt", encoding="utf-8") as f:
    file2_contents = f.read().splitlines()

comparator = difflib.HtmlDiff()
res = comparator.make_file(file1_contents, file2_contents)
with open("res.html", "w", encoding="utf-8") as f:
    f.write(res)
