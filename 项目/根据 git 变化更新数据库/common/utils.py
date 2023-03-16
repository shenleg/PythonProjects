import os


def get_json(data_dir_path):
    """
    获取 json 文件
    :param data_dir_path: 文件夹路径
    :return: all_files 列表，存放json文件
    """
    all_files = []
    for root, dirs, files in os.walk(data_dir_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)  # 合并成一个完整路径
            if file_name.endswith('.json'):  # 判断文件后缀是不是json
                all_files.append(file_path)
    return all_files
