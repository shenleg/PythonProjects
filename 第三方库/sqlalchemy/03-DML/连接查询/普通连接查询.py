from sqlalchemy import or_

from 第三方库.sqlalchemy.common.database import UsingAlchemy
from 第三方库.sqlalchemy.common.models import Student, Teacher

with UsingAlchemy() as ua:
    # 内连接
    # 结果只包含一个
    query = ua.session.query(Student).join(Teacher, Student.t_id == Teacher.id)
    print(query)
    # 补上其他结果
    query = ua.session.query(Student).join(Teacher, Student.t_id == Teacher.id).add_entity(Teacher)
    print(query)

    # 外连接
    query = ua.session.query(Student).outerjoin(Teacher, Student.t_id == Teacher.id)
    print(query)
    query = ua.session.query(Student).outerjoin(Teacher, Student.t_id == Teacher.id).add_entity(Teacher)
    print(query)
    query = ua.session.query(Student).outerjoin(Teacher, Student.t_id == Teacher.id).add_entity(Teacher).all()
    for item1, item2 in query:
        print(item1, item2)
    query = ua.session.query(Teacher).outerjoin(Student, Student.t_id == Teacher.id).add_entity(Student).all()
    for item1, item2 in query:
        print(item1, item2)

    # 加上筛选
    query = ua.session.query(Student).outerjoin(
        Teacher, Student.t_id == Teacher.id
    ).filter(
        or_(Student.id == 1, Student.id == 3)
    ).add_entity(Teacher)
    print(query)
    for student, teacher in query.all():
        print(student, teacher)

