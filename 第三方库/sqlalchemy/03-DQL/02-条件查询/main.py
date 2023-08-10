from sqlalchemy import or_, and_, not_

from 第三方库.sqlalchemy.common.database import UsingAlchemy
from 第三方库.sqlalchemy.common.models import Student

with UsingAlchemy() as ua:
    # 比较运算符
    # filter 非等值比较、逻辑运算符
    query = ua.session.query(Student).filter(
        Student.id == 1, Student.id != "1", Student.id > 1,
        Student.id < 1, Student.id >= 1, Student.id <= 1,
    )
    print("filter比较运算符", str(query))
    # filter_by 简单的相等性比较查询
    query = ua.session.query(Student).filter_by(id=1, name="张三")
    print("filter_by比较运算符", str(query))

    # AND
    # 使用filter默认就是and，多个参数形式
    query = ua.session.query(Student).filter(
        Student.id == 1, Student.name == "张三"
    )
    print("and_filter1", str(query))
    # 使用filter默认就是and，多个filter形式
    query = ua.session.query(Student).filter(
        Student.id == 1).filter(Student.name == "张三")
    print("and_filter2", str(query))
    # 使用 and_
    query = ua.session.query(Student).filter(
        and_(Student.id == 1, Student.name == "张三")
    )
    print("and_filter3", str(query))

    # OR
    query = ua.session.query(Student).filter(
        or_(Student.id == 1, Student.id == 4)
    )
    print("or_filter", str(query))

    # NOT
    query = ua.session.query(Student).filter(
        not_(Student.id == 1)
    )
    print("not_filter", str(query))

    # 多条件查询
    student_id = None
    student_name = "张三"
    student_age = 18
    query = ua.session.query(Student).filter(
        or_(Student.id == student_id, student_id is None),
        or_(Student.name == student_name, student_name is None),
        or_(Student.age == student_age, student_age is None),
    )
    print("多条件查询1", str(query))
