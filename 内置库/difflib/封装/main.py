import difflib
 
 
class DiffFile:
    """文件比较类"""
 
    @classmethod
    def _read_file(cls, file):
        """
        读取文件内容，以列表形式返回
        :param file: 文件路径
        :return:
        """
        try:
            with open(file, "r", encoding="utf-8") as fp:
                # 按行进行分割
                text = fp.read().splitlines()
                return text
        except Exception as e:
            print("ERROR: %s" % str(e))
 
    @classmethod
    def compare_file(cls, file1, file2, out_file):
        """
        比较文件，生成html格式
        :param file1: str 第1个文件路径
        :param file2: str 第2个文件路径
        :param out_file: str 比较结果文件路径
        :return:
        """
        file1_content = cls._read_file(file1)
        file2_content = cls._read_file(file2)
        comparator = difflib.HtmlDiff()
        compare_result = comparator.make_file(file1_content, file2_content)
        with open(out_file, 'w', encoding="utf-8") as fp:
            fp.write(compare_result)
 
    @classmethod
    def compare_text(cls, src_text, target_text):
        """
        比较给定的2个字符串
        :param src_text: str
        :param target_text: str
        :return:
        """
        d = difflib.Differ()
        return "".join(list(d.compare(src_text, target_text)))
 
    @classmethod
    def compare_text_to_file(cls, src_text, target_text, out_file):
        """
        比较给定的2个字符串，生成html格式
        :param src_text:
        :param target_text:
        :param out_file:
        :return:
        """
        compare = difflib.HtmlDiff()
        compare_result = compare.make_file(src_text, target_text)
        with open(out_file, 'w', encoding="utf-8") as fp:
            fp.write(compare_result)
 
 
if __name__ == '__main__':
    DiffFile.compare_file('a.txt',  "b.txt",  'diff.html')
 
    text1 = '''  1. Beautiful is better than ugly.
           2. Explicit is better than implicit.
           3. Simple is better than complex.
           4. Complex is better than complicated.
         '''.splitlines()
 
    text2 = '''  1. Beautiful is better than ugly.
           3.   Simple is better than complex.
           4. Complicated is better than complex.
           5. Flat is better than nested.
         '''.splitlines()
    DiffFile.compare_text_to_file(text1, text2, 'text_diff.html')
