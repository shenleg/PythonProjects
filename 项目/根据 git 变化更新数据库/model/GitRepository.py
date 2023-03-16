"""
Python 3.10
作者：张云辉
创建日期：2022年07月06日 17点47分
修改日期：
"""
import os

import git


class GitRepository:
    def __init__(self, local_path, remote_info, branch='main'):
        self.local_path = local_path
        self.remote_info = remote_info
        self.repo = None
        self.initial(remote_info, branch)

    def initial(self, remote_info, branch):
        """
        初始化仓库

        :param remote_info: 仓库信息：URL、用户名、密码
        :param branch: 分支名称，默认 main
        :return:
        """
        remote_url = "http://{}:{}@{}".format(
            remote_info["username"], remote_info["password"],
            remote_info["remote_http"].split("//")[1]
        )

        if not os.path.exists(self.local_path):
            os.makedirs(self.local_path)
            self.repo = git.Repo.clone_from(
                remote_url, to_path=self.local_path, branch=branch
            )
        else:
            self.repo = git.Repo(self.local_path)

    def pull(self):
        """
        从线上拉最新代码\n
        能强制移动 HEAD 到最新提交，忽略本地所有操作
        """
        self.repo.git.pull()
        self.repo.git.reset('--hard', "HEAD")

    def get_branch_list(self):
        """
        获取所有分支
        """
        branches = self.repo.remote().refs
        return [item.remote_head for item in branches if
                item.remote_head not in ['HEAD', ]]

    def get_tag_list(self):
        """
        获取所有 tag
        """
        tag_obj = sorted(self.repo.tags, key=lambda t: t.commit.committed_date)
        tag_obj = reversed(tag_obj)
        return [tag.name for tag in tag_obj]

    def change_to_branch(self, branch, force=False):
        """
        切换分支，代码为最新提交\n
        未 commit 时报错

        :param branch: 分支名称
        :param force: 是否强制切换
        :return:
        """
        self.repo.git.checkout(branch, force=force)

    def change_to_tag(self, tag):
        """
        切换tag

        :param tag:
        :return:
        """
        self.repo.git.checkout(tag)

    def get_commit_log(self, max_count=50):
        """
        获取所有提交记录

        :return: 提交记录，json字符串形式列表
        """
        commit_log = self.repo.git.log(
            '--pretty='
            '{"commit":"%h","author":"%an","summary":"%s","date":"%cd"}',
            max_count=max_count,
            date='format:%Y-%m-%d %H:%M'
        )
        log_list = commit_log.split("\n")
        return log_list

    def change_to_commit(self, branch, commit):
        """
        切换 commit

        :param branch: 先切换到分支
        :param commit: 提交 hash
        :return:
        """
        self.change_to_branch(branch)
        self.repo.git.reset('--hard', commit)

    def package(self, file_path):
        """
        打包代码

        :param file_path: 要打包的文件路径，已存在则覆盖
        """
        with open(file_path, 'wb') as f:
            self.repo.archive(f)


if __name__ == '__main__':
    dir_path = os.path.dirname(__file__)
    local_path = os.path.join(dir_path, 'so_old')

    remote_info = {
        "username": "zhangyunhui",
        "password": "zyh0921,",
        "remote_http": "http://10.101.4.30/grp-solveralgorithms/resolvebyso.git"
    }
    repo = GitRepository(local_path, remote_info)
    branch_list = repo.get_branch_list()
    print(branch_list)
    repo.change_to_branch('main', force=True)
    repo.pull()
