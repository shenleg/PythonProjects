from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from timeit import default_timer

from common import config

db_info = config.db_info["MySQL"]

url = db_info["sqlalchemy_url_format"].format(
    db_info["username"], db_info["password"], db_info["host"], db_info["port"],
    db_info["db"]
)

engine = create_engine(url, echo=False)

Session = sessionmaker(bind=engine, expire_on_commit=False)


class UsingAlchemy:

    def __init__(self, commit=True, log_time=False):
        """
        :param commit: 是否在最后提交事务(设置为False的时候方便单元测试)
        :param log_time:  是否打印程序运行总时间
        """
        self._commit = commit
        self._log_time = log_time
        self._session = Session()

    def __enter__(self):

        # 如果需要记录时间
        if self._log_time:
            self._start = default_timer()

        return self

    def __exit__(self, *exc_info):
        # 提交事务
        if self._commit:
            self._session.commit()

        if self._log_time:
            diff = default_timer() - self._start
            print('-- 总用时: {:.6f} 秒'.format(diff))

    @property
    def session(self):
        return self._session
