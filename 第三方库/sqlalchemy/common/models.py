"""
数据库模型表
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    # 定义表名
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)

    def __repr__(self):
        return "<id:{}, name:{}, age:{}>".format(self.id, self.name, self.age)
