"""
数据库模型表
"""
from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship

Base = declarative_base()


class Student(Base):
    # 定义表名
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)
    t_id = Column(Integer)

    def __repr__(self):
        return "<id:{}, name:{}, age:{}>".format(self.id, self.name, self.age)


class Teacher(Base):
    # 定义表名
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)

    def __repr__(self):
        return "<id:{}, name:{}, age:{}>".format(self.id, self.name, self.age)


# class Parent(Base):
#     __tablename__ = "parent"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     children: Mapped[List["Child"]] = relationship(back_populates="parent")
#
#
# class Child(Base):
#     __tablename__ = "child"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
#     parent: Mapped["Parent"] = relationship(back_populates="children")
