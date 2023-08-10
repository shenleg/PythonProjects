from sqlalchemy.orm import aliased

from 第三方库.sqlalchemy.common.database import UsingAlchemy
from 第三方库.sqlalchemy.common.models import Student

with UsingAlchemy() as ua:
    # 查询所有列
    query = ua.session.query(Student)
    print(query)  # 打印查询对象能直接显示sql构造，也可以通过str(query)转换
    for student in query:
        print(student.id, student.name, student.age)

    # 选择指定列
    query = ua.session.query(Student.name, Student.age)
    print(query)
    for name, age in query:
        print(name, age)

    # 类别名
    student_alias = aliased(Student)
    student_list = ua.session.query(student_alias, student_alias.name).all()
    for student in student_list:
        print(student)

    # 查询结果转换为列表，获取所有数据
    student_list = ua.session.query(Student.name, Student.age).all()
    for student in student_list:
        print(student)

    # 查询结果转换为列表，获取第一行
    student = ua.session.query(Student.name, Student.age).first()
    print(student)

    # 查询结果转换为列表，当且仅当只有一行，获取第一行，否则报错
    student = ua.session.query(Student.name, Student.age).filter(Student.id == 1).one()
    print(student)

    # 查询结果转换为列表，获取第一行第一列的值
    student_id = ua.session.query(Student.id).filter(Student.id == 1).scalar()
    print(student_id)
