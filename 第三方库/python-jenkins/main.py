"""
Python 3.10
作者：张云辉
创建日期：2023年03月17日 10点09分
修改日期：
"""

import jenkins


class JenkinsHelper:

    def __init__(self, url, username, password):
        self._url = url
        self._username = username
        self._password = password
        self._server = jenkins.Jenkins(self._url, username=self._username,
                                       password=self._password)

    def get_user(self):
        """用户信息"""
        return self._server.get_whoami()

    def get_version(self):
        """Jenkins 版本号"""
        return self._server.get_version()

    def get_jobs(self):
        """Jenkins job信息"""
        return {
            "jobs_count": self._server.jobs_count(),
            "get_jobs": self._server.get_jobs()
        }

    def job_exists(self, job_name):
        """根据 xml(str) 配置信息创建 job"""
        return self._server.job_exists(job_name)

    def create_job(self, job_name, config_xml=None):
        """根据 xml(str) 配置信息创建 job"""
        return self._server.create_job(job_name, config_xml)

    def copy_job(self, job_name, new_job_name):
        """复制 job"""
        return self._server.copy_job(job_name, new_job_name)

    def build_job(self, job_name, parameters=None, token=None):
        """根据参数(dict) 构建 job
           parameters like {"param_key": "param_value", ...}
        """
        return self._server.build_job(job_name, parameters, token)

    def other_job(self, job_name, number):
        """job 操作"""
        self._server.stop_build(job_name, number)  # 停止构建
        self._server.enable_job(job_name)  # 激活 job
        self._server.disable_job(job_name)  # 禁用 job
        self._server.delete_job(job_name)  # 删除 job

    def get_job_info(self, job_name):
        """获取 job 信息"""
        return self._server.get_job_info(job_name)

    def get_job_parameters(self, job_name):
        """获取 job Parameters 信息"""
        result = []
        for each in self.get_job_info(job_name)['property']:
            if 'ParametersDefinitionProperty' in each['_class']:
                data = each['parameterDefinitions']
                for params in data:
                    temp_dict = dict()
                    temp_dict['name'] = params['defaultParameterValue']['name']
                    temp_dict['value'] = params['defaultParameterValue']['value']
                    temp_dict['description'] = params['description']
                    result.append(temp_dict)
        return result

    def get_job_confing(self, job_name):
        """获取 job 的 xml(str) 配置信息"""
        return self._server.get_job_config(job_name)

    def get_build_info(self, job_name, number):
        """获取指定构建信息，详细信息
           result: UNSTABLE|SUCCESS
        """
        return self._server.get_build_info(job_name, number)

    def get_build_list(self, job_name):
        """获取构建列表，编号和 url"""
        return self._server.get_job_info(job_name)['build']

    def get_last_build(self, job_name):
        """获取最后一次构建"""
        number = self._server.get_job_info(job_name)['lastBuild']['number']
        return self._server.get_build_info(job_name, number)

    def get_build_console_output(self, job_name, number):
        """获取指定构建控制台输出"""
        return self._server.get_build_console_output(job_name, number)

    def delete_build(self, job_name, number):
        """删除指定构建"""
        return self._server.delete_build(job_name, number)

    def create_view(self, view_name):
        """创建视图"""
        self._server.create_view(
            view_name, config_xml=jenkins.EMPTY_VIEW_CONFIG_XML
        )

    def get_views(self):
        """获取视图列表"""
        return self._server.get_views()


def main():
    jenkins_url = "http://10.101.4.31:8080/jenkins"
    username = 'zhangyunhui'
    password = 'zhangyunhui123'

    job_name = "onlyTestCanBuild-so_compare"

    jenkins_server = JenkinsHelper(jenkins_url, username, password)

    job_info = jenkins_server.get_job_info(job_name)
    build_info = jenkins_server.get_build_info(job_name, 145)
    job_parameters = jenkins_server.get_job_parameters(job_name)

    print(1)


if __name__ == "__main__":
    main()
