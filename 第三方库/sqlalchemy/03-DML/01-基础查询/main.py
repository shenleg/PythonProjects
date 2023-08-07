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

    # 查询结果转换为列表
    student_list = ua.session.query(Student.name, Student.age).all()
    for student in student_list:
        print(student)

    # 类别名
    student_alias = aliased(Student)
    student_list = ua.session.query(student_alias, student_alias.name).all()
    for student in student_list:
        print(student)

