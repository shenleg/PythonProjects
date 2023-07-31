from 第三方库.sqlalchemy.common.database import UsingAlchemy
from 第三方库.sqlalchemy.common.models import Student

page_current = 1
page_size = 2
offset = page_size * (page_current - 1)
limit = page_size

with UsingAlchemy() as ua:
    student_list = ua.session.query(Student).all()
    print(student_list)

    student_list = ua.session.query(Student).offset(offset).limit(limit).all()
    print(student_list)
