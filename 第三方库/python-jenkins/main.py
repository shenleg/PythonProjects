"""
python-jenkins==1.7.0
urllib3==1.26.16
"""

import jenkins


class JenkinsHelper:

    def __init__(self, url, username, password):
        self._url = url
        self._username = username
        self._password = password
        self._server = jenkins.Jenkins(
            self._url, username=self._username, password=self._password)

    def get_view_list(self):
        """获取视图简单信息列表
        :return: list dict
        """
        return self._server.get_views()

    def get_job_list(self):
        """获取 job 简单信息列表
        :return: list dict
        """
        return self._server.get_jobs()

    def get_job_info(self, job_name):
        """获取 job 详细信息
        :return: dict
        """
        return self._server.get_job_info(job_name)

    def get_build_list(self, job_name):
        """获取构建简单信息列表
        :return: list dict
        """
        return self._server.get_job_info(job_name)["builds"]

    def get_build_info(self, job_name, number):
        """获取指定构建详细信息
        :return: dict
        """
        return self._server.get_build_info(job_name, number)

    def get_last_build_info(self, job_name):
        """获取最后一次构建详细信息
        :return: dict
        """
        number = self._server.get_job_info(job_name)['lastBuild']['number']
        return self._server.get_build_info(job_name, number)

    def get_build_params(self, job_name, number):
        """获取指定构建的构建参数
        :return: list dict
        """
        build_info = self.get_build_info(job_name, number)
        for each in build_info["actions"]:
            if "ParametersAction" in each["_class"]:
                return each["parameters"]

    def get_build_cause(self, job_name, number):
        """获取指定构建的构建参数
        :return: list dict
        """
        build_info = self.get_build_info(job_name, number)
        for each in build_info["actions"]:
            if "CauseAction" in each["_class"]:
                return each["causes"]

    def get_build_console_output(self, job_name, number):
        """获取指定构建控制台输出
        :return: str
        """
        return self._server.get_build_console_output(job_name, number)

    def delete_build(self, job_name, number):
        """删除指定构建"""
        return self._server.delete_build(job_name, number)


def main():
    jenkins_url = "http://10.30.0.11:8080/jenkins"
    username = 'zhangyunhui'
    password = 'zj0510,'

    job_name = "onlyTestCanBuild-so_compare"

    jenkins_server = JenkinsHelper(jenkins_url, username, password)

    job_list = jenkins_server.get_job_list()
    job_info = jenkins_server.get_job_info(job_name)


if __name__ == '__main__':
    main()
