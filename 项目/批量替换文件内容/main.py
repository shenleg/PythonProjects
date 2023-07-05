"""
Python 3.10
作者：张云辉
创建日期：2023年07月05日 14点03分
修改日期：
"""
import os


def get_file_list(path, file=False, dir=False, abs=True, deep=False, extension=None):
    """
    获取指定路径下的文件列表

    :param path: str 需要查找的路径
    :param file: bool 是否查找文件
    :param dir: bool 是否查找目录
    :param abs: bool 是否返回绝对路径
    :param deep: bool 是否深度搜索
    :param extension: str 过滤扩展名，支持多个
    :return: list 文件路径
    """
    if not os.path.exists(path):
        return "路径不存在"
    if deep:
        file_all = []
        dir_all = []
        both_all = []
        for root, dir_list, file_list in os.walk(path):
            if extension:
                file_list = list(filter(lambda x: x.split(".")[-1] in extension, file_list))
            if abs:
                dir_list = [os.path.join(root, d) for d in dir_list]
                file_list = [os.path.join(root, f) for f in file_list]
            if (file and dir) or (not file and not dir):
                both_all.extend(dir_list)
                both_all.extend(file_list)
            elif dir:
                dir_all.extend(dir_list)
            elif file:
                file_all.extend(file_list)
        if (file and dir) or (not file and not dir):
            return both_all
        elif dir:
            return dir_all
        elif file:
            return file_all
    else:
        for root, dir_list, file_list in os.walk(path):
            if extension:
                file_list = list(filter(lambda x: x.split(".")[-1] in extension, file_list))
            if abs:
                dir_list = [os.path.join(root, d) for d in dir_list]
                file_list = [os.path.join(root, f) for f in file_list]
            if (file and dir) or (not file and not dir):
                return dir_list + file_list
            elif dir:
                return dir_list
            elif file:
                return file_list

# 文件夹
direction_path = r"C:\Users\ZJ\Documents\MyGitProjects\blog_backup\source\_posts"
# 后缀名
extension = "md;more"

count = 0
file_list = get_file_list(direction_path, file=True, deep=True, extension=extension)
print(f"总共{len(file_list)}个文件")
for file in file_list:
    print(f"开始替换文件：{file}")
    with open(file, "r", encoding="utf-8") as f:
        res = f.read()
        res = res.replace("https://cdn", "http://cdn")

    with open(file, "w", encoding="utf-8") as f:
        f.write(res)
    count += 1
print(f"总共替换{count}个文件")




