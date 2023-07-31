"""
直接使用 Jenkins API
结论是Jenkins本身的API就很慢
"""
import time

import requests
from requests.auth import HTTPBasicAuth


class JenkinsHelper:

    def __init__(self, url, username, password):
        """

        :param url: str, like http://10.30.0.11:8080/jenkins
        :param username:
        :param password:
        """
        self._url = url
        self._auth = HTTPBasicAuth(username, password)

    def get_view_list(self):
        """获取视图简单信息列表
        :return: list dict
        """
        res = requests.get(self._url + "/api/json", auth=self._auth)
        return res.json()["view"]

    def get_job_list(self):
        """获取 job 简单信息列表
        :return: list dict
        """
        res = requests.get(self._url + "/api/json", auth=self._auth)
        return res.json()["jobs"]

    def get_job_info(self, job_name):
        """获取 job 详细信息
        :return: dict
        """
        res = requests.get(f"{self._url}/job/{job_name}/api/json", auth=self._auth)
        return res.json()

    def get_build_list(self, job_name):
        """获取构建简单信息列表
        :return: list dict
        """
        res = requests.get(f"{self._url}/job/{job_name}/api/json",
                           auth=self._auth)
        return res.json()["builds"]

    def get_build_info(self, job_name, number):
        """获取指定构建详细信息
        :return: dict
        """
        res = requests.get(f"{self._url}/job/{job_name}/{number}/api/json",
                           auth=self._auth)
        return res.json()

    def get_last_build_info(self, job_name):
        """获取最后一次构建详细信息
        :return: dict
        """
        number = self.get_job_info(job_name)['lastBuild']['number']
        return self.get_build_info(job_name, number)

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
        res = requests.get(f"{self._url}/job/{job_name}/{number}/consoleText",
                           auth=self._auth)
        return res.text


def main():
    jenkins_url = "http://10.30.0.11:8080/jenkins"
    username = 'zhangyunhui'
    password = 'zj0510,'

    job_name = "onlyTestCanBuild-so_compare"

    jenkins_server = JenkinsHelper(jenkins_url, username, password)

    job_list = jenkins_server.get_job_list()
    time_start = time.time()
    job_info = jenkins_server.get_job_info(job_name)
    print(time.time()-time_start)


if __name__ == '__main__':
    main()
