import json
import os
import re

from common import config, utils, setting
from model.GitRepository import GitRepository
from model.UsingAlchemy import UsingAlchemy
from model.Schema import Schema


def get_repo():
    # 拉取测试案例
    testcases_remote_info = config.git_info["TestCases"]
    testcases_local_path = setting.TESTCASES_REPO_PATH
    testcases_repo = GitRepository(testcases_local_path, testcases_remote_info)
    testcases_repo.pull()


def file2entity(dir_path):
    schema_list = []
    file_list = utils.get_json(dir_path)
    for file in file_list:
        schema_name = os.path.basename(file).split(".")[0]
        with open(file, "r", encoding="utf-8") as f:
            schema_content = json.load(f)
        # '图文件/01-电气/01-电源/3P-VAC-三相交流正弦电压源.json'
        path_partition = file.partition("图文件")
        file_path = "/".join(
            (path_partition[1] + path_partition[2]).split(os.path.sep)
        )
        subject = re.search(r"([\u4e00-\u9fa5]+)",
                            file_path.split("/")[1]).group(1)
        subject = config.subject_ch2en.get(subject, "combination")

        schema = Schema(
            schema_name=schema_name, schema_content=schema_content,
            subject=subject, file_path=file_path
        )
        schema_list.append(schema)
    return schema_list


def add():
    # 1. 把testcase拉取到本地
    get_repo()
    # 2. 获取本地图文件信息，组装成需要的实体列表
    schema_list = file2entity(
        os.path.join(setting.TESTCASES_REPO_PATH, "testcases")
    )
    # 3. 上传到数据库
    with UsingAlchemy() as ua:
        ua.session.add_all(schema_list)


def add_or_update():
    # 1. 把testcase拉取到本地
    get_repo()
    # 2. 获取本地图文件信息，组装成需要的实体列表
    schema_list = file2entity(
        os.path.join(setting.TESTCASES_REPO_PATH, "testcases"))
    # 3. 上传到数据库
    schema_id_list = []  # 记录本地id
    with UsingAlchemy() as ua:
        # 3.1 存在则更新，不存在则新增
        for schema in schema_list:
            res = ua.session.query(Schema).filter(
                Schema.schema_name == schema.schema_name
            ).first()
            # 3.1.1 存在则更新
            if res:
                ua.session.query(Schema).filter(
                    Schema.schema_name == schema.schema_name
                ).update(
                    {Schema.schema_content: schema.schema_content,
                     Schema.subject: schema.subject,
                     Schema.file_path: schema.file_path}
                )
                schema_id_list.append(res.schema_id)  # 记录本地id
            # 3.1.2 不存在则新增
            else:
                ua.session.add(schema)
                ua.session.flush()
                schema_id_list.append(schema.schema_id)  # 记录本地id
        # 3.2 删除掉过期的图文件
        ua.session.query(Schema).filter(
            Schema.schema_id.notin_(schema_id_list)
        ).delete()


def main():
    # 存在则更新，不存在则新增
    add_or_update()


if __name__ == "__main__":
    main()
