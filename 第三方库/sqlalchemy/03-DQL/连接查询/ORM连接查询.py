from sqlalchemy import Column, Integer, String, or_
from sqlalchemy.orm import declarative_base, relationship

from 第三方库.sqlalchemy.common.database import UsingAlchemy

Base = declarative_base()


class Student(Base):
    # 定义表名
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)
    t_id = Column(Integer)

    teacher = relationship("Teacher", back_populates="user")


class Teacher(Base):
    # 定义表名
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)



with UsingAlchemy() as ua:
    # 内连接
    # 结果只包含一个
    query = ua.session.query(Student).join(Teacher, Student.t_id == Teacher.id)
    print(query)
    # 补上其他结果
    query = ua.session.query(Student).join(Teacher,
                                           Student.t_id == Teacher.id).add_entity(
        Teacher)
    print(query)

    # 外连接
    query = ua.session.query(Student).outerjoin(Teacher,
                                                Student.t_id == Teacher.id)
    print(query)
    query = ua.session.query(Student).outerjoin(Teacher,
                                                Student.t_id == Teacher.id).add_entity(
        Teacher)
    print(query)

    # 加上筛选
    query = ua.session.query(Student).outerjoin(
        Teacher, Student.t_id == Teacher.id
    ).filter(
        or_(Student.id == 1, Student.id == 3)
    ).add_entity(Teacher)
    print(query)
    for student, teacher in query.all():
        print(student, teacher)
