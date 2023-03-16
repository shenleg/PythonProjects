import json
import os
import re
import subprocess

from common import setting
from model.Schema import Schema
from model.UsingAlchemy import UsingAlchemy
from model.GitRepository import GitRepository
from common import config


def get_repo():
    # 拉取测试案例
    testcases_remote_info = config.git_info["TestCases"]
    testcases_local_path = setting.TESTCASES_REPO_PATH
    testcases_repo = GitRepository(testcases_local_path, testcases_remote_info)
    testcases_repo.pull()


def get_change_list():
    command = r"cd {} && git log -1 --name-status".format(
        setting.TESTCASES_REPO_PATH)
    print("command", command)
    code, res = subprocess.getstatusoutput(command)
    print("code", code)
    print("res", res)

    author = re.search(r"Author: ([\S.]+)\s", res).group(1)

    change_str = res.split("\n\n")[2].split("\n")
    change_list = []
    for line in change_str:
        change_list.append((line[0], re.findall(r'"(.+?)"', line)))

    for mode, file_list in change_list:
        for i, file in enumerate(file_list):
            file_list[i] = eval(f'b"{file}".decode("utf-8")')

    return author, change_list


def add_schema(author, git_schema_path):
    """
    A：增加
    :param author:
    :param git_schema_path: # 图文件/01-电气/04-半导体/xxx 图文件.json
    :return:
    """
    schema_name = os.path.basename(git_schema_path).split(".")[0]
    # 0. 不存在再添加，防止重复添加
    with UsingAlchemy() as ua:
        # 1. 查询到id
        res = ua.session.query(Schema).filter(
            Schema.schema_name == schema_name
        ).first()
        if res:
            return
    # 1. 读取本地图文件
    os_schema_path = os.path.sep.join(git_schema_path.split("/"))
    schema_path = os.path.join(setting.TESTCASES_REPO_PATH, os_schema_path)
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_content = json.load(f)
    file_path = git_schema_path
    subject = re.search(r"([\u4e00-\u9fa5]+)", file_path.split("/")[1]).group(1)
    subject = config.subject_ch2en.get(subject, "combination")
    # 2. 添加到数据库中
    schema = Schema(
        schema_name=schema_name, schema_content=schema_content,
        subject=subject, file_path=file_path, created_by=author,
        updated_by=author
    )
    with UsingAlchemy() as ua:
        ua.session.add(schema)


def modify_schema(author, git_schema_path):
    """
    M：修改
    :param author:
    :param git_schema_path: # 图文件/01-电气/04-半导体/xxx 图文件.json
    :return:
    """
    # 1. 读取本地图文件
    os_schema_path = os.path.sep.join(git_schema_path.split("/"))
    schema_path = os.path.join(setting.TESTCASES_REPO_PATH, os_schema_path)
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_content = json.load(f)
    schema_name = os.path.basename(git_schema_path).split(".")[0]
    # 2. 更新到数据库中
    with UsingAlchemy() as ua:
        ua.session.query(Schema).filter(
            Schema.schema_name == schema_name
        ).update(
            {Schema.schema_content: schema_content, Schema.updated_by: author}
        )


def delete_schema(git_schema_path):
    """
    D：删除
    :param git_schema_path: # 图文件/01-电气/04-半导体/xxx 图文件.json
    :return:
    """
    schema_name = os.path.basename(git_schema_path).split(".")[0]
    with UsingAlchemy() as ua:
        # 1. 查询到id
        res = ua.session.query(Schema).filter(
            Schema.schema_name == schema_name
        ).first()
        # 2. 从数据库中删除
        if res:
            ua.session.query(Schema).filter(
                Schema.schema_id == res.schema_id
            ).delete()
            # 3. 级联删除参数表 # TODO


def replace_schema(author, old_git_schema_path, new_git_schema_path):
    """
    R：路径变化，在原来数据（id）上更新，而不是删除后新增
    :param author:
    :param old_git_schema_path: # 图文件/01-电气/04-半导体/xxx 图文件.json
    :param new_git_schema_path: # 图文件/02-控制/01-基础元件/xxx 图文件.json
    :return:
    """
    # 1. 读取新的文件信息
    os_schema_path = os.path.sep.join(new_git_schema_path.split("/"))
    new_schema_path = os.path.join(setting.TESTCASES_REPO_PATH, os_schema_path)
    with open(new_schema_path, "r", encoding="utf-8") as f:
        new_schema_content = json.load(f)
    new_schema_name = os.path.basename(new_schema_content).split(".")[0]
    new_file_path = new_git_schema_path
    new_subject = re.search(
        r"([\u4e00-\u9fa5]+)", new_file_path.split("/")[1]
    ).group(1)
    new_subject = config.subject_ch2en.get(new_subject, "combination")

    old_schema_name = os.path.basename(old_git_schema_path).split(".")[0]
    with UsingAlchemy() as ua:
        # 2. 从数据库中找出原来的id
        res = ua.session.query(Schema).filter(
            Schema.schema_name == old_schema_name
        ).first()
        # 3. 更新新的到数据库中
        ua.session.query(Schema).filter(
            Schema.schema_id == res.schema_id
        ).update(
            {Schema.schema_name: new_schema_name, Schema.subject: new_subject,
             Schema.file_path: new_file_path, Schema.updated_by: author}
        )


def main():
    # 1. 把testcase拉取到本地
    get_repo()
    # 2. 获取更新信息
    author, change_list = get_change_list()
    print("author", author)
    print("change_list")
    for change_line in change_list:
        print(change_line)
        stat = change_line[0]
        if stat == "A":
            add_schema(author, change_line[1][0])
        elif stat == "M":
            modify_schema(author, change_line[1][0])
        elif stat == "D":
            delete_schema(change_line[1][0])
        elif stat == "R":
            replace_schema(author, change_line[1][0], change_line[1][1])
    print("执行成功")


if __name__ == '__main__':
    main()
