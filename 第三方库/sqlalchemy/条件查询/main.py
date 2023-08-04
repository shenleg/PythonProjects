from sqlalchemy import or_

from 第三方库.sqlalchemy.common.database import UsingAlchemy
from 第三方库.sqlalchemy.common.models import Student

with UsingAlchemy() as ua:
    student_list = ua.session.query(Student).all()
    print("all", student_list)

    student_list = ua.session.query(Student).filter(
        or_(Student.id == 1, Student.id is None)
    ).all()
    print("filter1", student_list)

    student_id = None
    student_name = None
    student_age = None
    student_list = ua.session.query(Student).filter(
        or_(Student.id == student_id, Student.name == student_name, Student.age == student_age)
        # or_(Student.name == student_name),
        # or_(Student.age == student_age),
    ).all()
    print("filter2", student_list)
