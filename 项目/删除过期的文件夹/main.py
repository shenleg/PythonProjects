import os
import shutil
import time


def get_file_list(dir_path, file=False, dir=False, abs=False, deep=False):
    """
    获取指定路径下的文件列表
    :param dir_path:
    :param file: bool 是否需要文件列表
    :param dir: bool 是否需要文件夹列表
    :param abs: bool 是否需要加上绝对路径
    :param deep: 是否递归搜索
    :return:
    """
    if not os.path.isabs(dir_path):
        return "只能传绝对路径"
    if not os.path.exists(dir_path):
        return "路径不存在"
    if deep:
        file_all = []
        dir_all = []
        both_all = []
        for root, dir_list, file_list in os.walk(dir_path):
            if abs:
                dir_list = [os.path.join(root, d) for d in dir_list]
                file_list = [os.path.join(root, f) for f in file_list]
            if (file and dir) or (not file and not dir):  # 默认全部都要
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
        for root, dir_list, file_list in os.walk(dir_path):
            if abs:
                dir_list = [os.path.join(root, d) for d in dir_list]
                file_list = [os.path.join(root, f) for f in file_list]
            if (file and dir) or (not file and not dir):
                return dir_list + file_list
            elif dir:
                return dir_list
            elif file:
                return file_list


def del_outdated_dir(dir_path, count):
    """
    删除指定路径下的过期文件夹
    :param dir_path: str 路径
    :param count: int 过期几天
    :return:
    """
    dir_list = get_file_list(dir_path, dir=True, abs=True)
    now = int(time.strftime("%Y%m%d"))
    dir_outdated_list = []
    for d in dir_list:
        basename = os.path.basename(d)
        if basename.isdigit() and int(basename) <= now - count:
            dir_outdated_list.append(d)
    for d in dir_outdated_list:
        shutil.rmtree(d)


if __name__ == '__main__':
    path = r"C:\Users\ZJ\Documents\PycharmProjects\pythonProject\项目\删除指定日期前的文件夹"
    del_outdated_dir(path, 5)


